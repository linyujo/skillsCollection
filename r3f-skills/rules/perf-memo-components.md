# perf-memo-components

---

title: Memoize expensive components.
impact: CRITICAL
impactDescription: Prevents re-renders if props haven't changed.

---

## Good Example

```jsx
// GOOD - Prevents re-renders if props haven't changed

const ExpensiveModel = memo(function ExpensiveModel({ url }) {
  const { scene } = useGLTF(url);
  return <primitive object={scene.clone()} />;
});
```

## Good Example 2

```jsx
// With custom comparison

const OptimizedMesh = memo(
  function OptimizedMesh({ position, color }) {
    return (
      <mesh position={position}>
        <boxGeometry />
        <meshStandardMaterial color={color} />
      </mesh>
    );
  },
  (prev, next) => {
    return (
      prev.color === next.color &&
      prev.position[0] === next.position[0] &&
      prev.position[1] === next.position[1] &&
      prev.position[2] === next.position[2]
    );
  },
);
```
