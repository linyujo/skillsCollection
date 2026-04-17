# frame-delta-time

---

title: Always use delta for frame-rate independent animation.
impact: CRITICAL

---

## Bad Example

```jsx
// BAD - Speed varies with frame rate

function BadAnimation() {
  useFrame(() => {
    ref.current.rotation.y += 0.01; // Moves faster on faster computers
  });
}
```

## Good Example

```jsx
// GOOD - Consistent speed on all devices

function GoodAnimation() {
  useFrame((state, delta) => {
    ref.current.rotation.y += 1 * delta; // Moves at same speed on all computers
  });
}
```

## Good Example 2

```jsx
// GOOD - Using clock for time-based effects

useFrame(({ clock }) => {
  ref.current.position.y = Math.sin(clock.elapsedTime) * 2;
});
```

## Good Example 3 - Frame-rate Independent Lerp

```jsx
function SmoothFollow({ target }) {
  useFrame((state, delta) => {
    // Frame-rate independent smooth interpolation
    const lerpFactor = 1 - Math.pow(0.001, delta);
    ref.current.position.lerp(target, lerpFactor);
  });
}
```

## Good Example 4 - Movement with Speed

```jsx
function MovingObject() {
  const meshRef = useRef();
  const speed = 5; // units per second
  const direction = useRef(new THREE.Vector3(1, 0, 0));

  useFrame((state, delta) => {
    meshRef.current.position.addScaledVector(direction.current, speed * delta);
  });

  return <mesh ref={meshRef} />;
}
```

## Good Example 5 - Combining Delta and Elapsed Time

```jsx
function ComplexAnimation() {
  const meshRef = useRef();

  useFrame(({ clock }, delta) => {
    const t = clock.elapsedTime;

    // Position based on elapsed time (consistent patterns)
    meshRef.current.position.x = Math.sin(t) * 3;
    meshRef.current.position.z = Math.cos(t) * 3;

    // Rotation based on delta (consistent speed)
    meshRef.current.rotation.y += 0.5 * delta;
  });

  return <mesh ref={meshRef} />;
}
```
