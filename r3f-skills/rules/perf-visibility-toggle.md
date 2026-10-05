# perf-visibility-toggle

---

title: Toggle Visibility Instead of Remounting.
impact: CRITICAL
impactDescription: Toggle the visible prop instead of conditionally mounting/unmounting components.

---

## Why It Matters

Remounting a component:

1. Destroys the Three.js object
2. Disposes its geometry / material
3. Creates new geometry / material
4. Uploads new data to the GPU
5. Recompiles shaders

## Bad Example

```jsx
// BAD - Conditional mounting rebuilds everything on every toggle
function Scene({ showModel }) {
  return <>{showModel && <ExpensiveModel />}</>;
}
```

## Good Example

```jsx
// GOOD - Toggle visibility, the object and its GPU resources stay alive
function Scene({ showModel }) {
  return <ExpensiveModel visible={showModel} />;
}
```

For toggles driven every frame (e.g. by distance), set `ref.current.visible` inside `useFrame` instead of going through React state.

## Good Example 2 - Layers

Layers decide which camera renders an object without touching `visible`.

```jsx
// GOOD - Only cameras with layer 1 enabled render this mesh
function SelectiveRendering() {
  const meshRef = useRef();

  useEffect(() => {
    meshRef.current.layers.set(1);
  }, []);

  return <mesh ref={meshRef} />;
}
```

The default camera only sees layer 0, so after `layers.set(1)` the mesh disappears from the main view until a camera calls `camera.layers.enable(1)`. The raycaster also only tests layer 0 by default.

## Use Visibility Toggle When

- Frequent show/hide (e.g., UI state)
- Object is expensive to create
- Object is needed again soon

## Use Remounting When

- Object is rarely shown
- Memory is constrained
- Object is cheap to create
- Large number of potential objects

## References

- [100 Three.js Tips - Utsubo](https://www.utsubo.com/blog/threejs-best-practices-100-tips)
