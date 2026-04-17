# perf-visibility-toggle

---

title: Toggle Visibility Instead of Remounting.
impact: CRITICAL
impactDescription: Toggle the visible prop instead of conditionally mounting/unmounting components.

---

## Why It Matters

Remounting a component:

1. Destroys the Three.js object
2. Triggers disposal (if configured)
3. Creates new geometry/material
4. Uploads new data to GPU
5. Recompiles shaders

## Bad Example

```jsx
// BAD - Conditional Mounting

function Scene({ showModel }) {
  return <>{showModel && <ExpensiveModel />}</>;
}
```

## Good Example

```jsx
// GOOD - Toggle Visibility

function Scene({ showModel }) {
  return <ExpensiveModel visible={showModel} />;
}
```

## Good Example 2

```jsx
// GOOD - Toggle Visibility With Refs

function ToggleableModel() {
  const meshRef = useRef();
  const [visible, setVisible] = useState(true);

  // Direct mutation for animations
  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.visible = shouldBeVisible;
    }
  });

  return <mesh ref={meshRef} visible={visible} />;
}
```

## Good Example 3

For complex visibility logic, consider using Three.js layers.
Layers allow camera-selective rendering without changing visibility.

```jsx
// GOOD - Layers allow camera-selective rendering without changing visibility.

function SelectiveRendering() {
  const meshRef = useRef();

  useEffect(() => {
    // Set to layer 1 (not rendered by default camera)
    meshRef.current.layers.set(1);
  }, []);

  return <mesh ref={meshRef} />;
}
```

## Use Visibility Toggle When

- Frequent show/hide (e.g., UI state)
- Object is expensive to create
- Object is needed again soon
- Object count is manageable

## When NOT to Use Visibility Toggle

- Object is rarely shown
- Memory is constrained
- Object is cheap to create
- Large number of potential objects

## References

- [100 Three.js Tips - Utsubo](https://www.utsubo.com/blog/threejs-best-practices-100-tips)
