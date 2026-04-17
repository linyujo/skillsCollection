# frame-render-on-demand

---

title: Use invalidate() for on-demand rendering.
impact: CRITICAL

---

## Good Example

```jsx
// Enable frameloop="demand" on Canvas
<Canvas frameloop="demand">
  <Scene />
</Canvas>;

// Manually request render when needed
function OnDemandAnimation() {
  const { invalidate } = useThree();

  const handleClick = () => {
    // Trigger single render
    invalidate();
  };

  // Or invalidate in response to external events
  useEffect(() => {
    const unsubscribe = someStore.subscribe(() => {
      invalidate();
    });
    return unsubscribe;
  }, [invalidate]);
}
```
