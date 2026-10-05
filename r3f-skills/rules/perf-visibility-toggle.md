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
