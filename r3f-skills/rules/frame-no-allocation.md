# frame-no-allocation

---

title: Don't allocate objects inside useFrame.
impact: CRITICAL
impactDescription: useFrame runs 60-120 times per second. Every new Vector3 / Quaternion / Matrix4 / array created there becomes garbage, and periodic garbage collection shows up as frame drops.

---

## Bad Example

```jsx
// BAD - 3 new objects per frame per component
function Follower({ target }) {
  const ref = useRef();

  useFrame((_, delta) => {
    const goal = new THREE.Vector3(target.x, target.y + 1, target.z); // new
    const dir = goal.clone().sub(ref.current.position); // new
    ref.current.position.add(dir.multiplyScalar(delta));
    ref.current.quaternion.slerp(new THREE.Quaternion(), delta); // new
  });

  return <mesh ref={ref} />;
}
```

Common hidden allocations: `new THREE.*()`, `.clone()`, `[...array]`, `array.map()` / `filter()`, object literals `{ x, y }`, `getWorldPosition(new THREE.Vector3())`.

## Good Example 1 - Scratch objects at module level

```jsx
// GOOD - Allocated once, reused every frame (safe: useFrame callbacks run one at a time)
const _goal = new THREE.Vector3();
const _dir = new THREE.Vector3();
const _identity = new THREE.Quaternion();

function Follower({ target }) {
  const ref = useRef();

  useFrame((_, delta) => {
    _goal.set(target.x, target.y + 1, target.z);
    _dir.subVectors(_goal, ref.current.position).multiplyScalar(delta);
    ref.current.position.add(_dir);
    ref.current.quaternion.slerp(_identity, delta);
  });

  return <mesh ref={ref} />;
}
```

## Good Example 2 - Per-instance scratch objects

Use `useMemo` / `useRef` when the value must persist per component between frames (module-level scratch objects are shared by all instances):

```jsx
function Tracker() {
  const ref = useRef();
  const lastPosition = useMemo(() => new THREE.Vector3(), []);

  useFrame(() => {
    const speed = ref.current.position.distanceTo(lastPosition);
    lastPosition.copy(ref.current.position);
    // ...
  });

  return <mesh ref={ref} />;
}
```

## Notes

- Prefer three's in-place methods: `.set()`, `.copy()`, `.subVectors()`, `.lerp()`, `getWorldPosition(target)` with a reused `target`.
- Check with the browser profiler's memory timeline: a steady sawtooth pattern while the scene is idle usually means per-frame allocations.
