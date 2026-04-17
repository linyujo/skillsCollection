# frame-avoid-heavy-computation

---

title: Move heavy computations outside useFrame.
impact: CRITICAL

---

## Bad Example

```jsx
// BAD - Expensive calculation every frame

function BadAnimation({ mesh }) {
  useFrame((state, delta) => {
    // Heavy computation - runs every frame
    const expensiveResult = heavyComputation(); // 60x per second!
    ref.current.position.copy(expensiveResult);
  });
}
```

## Good Example

```jsx
// GOOD - Heavy computation outside useFrame

function GoodAnimation({ mesh }) {
  const [targetPosition, setTargetPosition] = useState(new THREE.Vector3());

  // Update target occasionally
  useEffect(() => {
    const interval = setInterval(() => {
      setTargetPosition(heavyComputation());
    }, 100); // 10 times per second
    return () => clearInterval(interval);
  }, []);

  // Lerp to target every frame (cheap)
  useFrame(() => {
    ref.current.position.lerp(targetPosition, 0.1);
  });
}
```
