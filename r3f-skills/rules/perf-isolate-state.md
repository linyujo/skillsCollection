# perf-isolate-state

---

title: Isolate components that need React state.
impact: CRITICAL
impactDescription: Entire scene re-renders when state changes

---

## Bad Example

```jsx
// BAD - Entire scene re-renders when score changes
function Game() {
  const [score, setScore] = useState(0);

  return (
    <>
      <HUD score={score} />
      <Player />
      <Enemies count={100} /> {/* Re-renders when score changes! */}
      <Environment />
    </>
  );
}
```

## Good Example

```jsx
// GOOD - Only HUD Component re-renders
function Game() {
  return (
    <>
      <HUD /> {/* Manages its own state or uses store */}
      <Player />
      <Enemies count={100} />
      <Environment />
    </>
  );
}

function HUD() {
  const score = useGameStore((state) => state.score);
  return (
    <Html>
      <div>{score}</div>
    </Html>
  );
}
```
