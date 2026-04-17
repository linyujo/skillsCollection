# perf-avoid-inline-objects

---

title: Avoid creating new objects/arrays in JSX.
impact: CRITICAL
impactDescription: Inline objects/arrays create new references on every render, causing unnecessary re-renders and prop comparisons.

---

## Bad Example

```jsx
// BAD - New array created every render

function BadMesh() {
  return <mesh position={[1, 2, 3]} />; // New array each render
}
```

## Good Example

```jsx
// GOOD - Stable reference

const POSITION = [1, 2, 3];
function GoodMesh() {
  return <mesh position={POSITION} />;
}
```

## Good Example 2

```jsx
// GOOD - Using individual props

function GoodMesh() {
  return <mesh position-x={1} position-y={2} position-z={3} />;
}
```

## Good Example 3

```jsx
// GOOD - useMemo for computed values

function ComputedMesh({ x }) {
  const position = useMemo(() => [x, x * 2, x * 3], [x]);
  return <mesh position={position} />;
}
```
