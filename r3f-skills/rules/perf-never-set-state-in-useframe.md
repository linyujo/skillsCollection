# perf-never-set-state-in-useframe

---

title: NEVER call setState inside useFrame.
impact: CRITICAL
impactDescription: This is the #1 performance killer in R3F. Calling setState triggers React re-renders. useFrame runs at 60fps. setState in useFrame = 60 re-renders per second = destroyed performance.

---

## Bad Example

```jsx
// BAD - Causes 60 re-renders per second!
function BadComponent() {
  const [position, setPosition] = useState(0);

  useFrame(() => {
    setPosition((p) => p + 0.01); // NEVER DO THIS
  });

  return <mesh position-x={position} />;
}
```

This triggers React reconciliation 60 times per second, causing:

Massive CPU usage
Frame drops
Component re-creation
Garbage collection pauses

## Good Example

```jsx
// GOOD - Mutate refs directly, no re-renders
function GoodComponent() {
  const meshRef = useRef();

  useFrame(() => {
    meshRef.current.position.x += 0.01;
  });

  return <mesh ref={meshRef} />;
}
```

The ref gives direct access to the Three.js object. Mutating it doesn't trigger React.
