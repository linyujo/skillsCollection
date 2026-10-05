# frame-render-on-demand

---

title: Use invalidate() for on-demand rendering.
impact: CRITICAL

---

## frameloop modes

```jsx
<Canvas frameloop="always">  {/* Default: render every frame */}
<Canvas frameloop="demand">  {/* Render only after invalidate() */}
<Canvas frameloop="never">   {/* Never render by itself, drive it with advance() */}
```

With `frameloop="demand"`, R3F renders when props change through React and when `invalidate()` is called. Anything that mutates the scene **outside React** must call `invalidate()` itself, or the change never reaches the screen.

## Bad Example

```jsx
// BAD - Two problems
function Door() {
  const { invalidate } = useThree(); // 1. No selector: re-renders on every store change (resize, etc.)
  const ref = useRef();

  useEffect(() => {
    return useDoorStore.subscribe((s) => {
      ref.current.rotation.y = s.angle; // 2. Mutated outside React, no invalidate → screen not updated
    });
  }, []);

  return <mesh ref={ref} />;
}
```

## Good Example

```jsx
// GOOD - Select only invalidate, call it after every outside mutation
function Door() {
  const invalidate = useThree((s) => s.invalidate);
  const ref = useRef();

  useEffect(() => {
    return useDoorStore.subscribe((s) => {
      ref.current.rotation.y = s.angle;
      invalidate();
    });
  }, [invalidate]);

  return <mesh ref={ref} />;
}
```

## Mutations that need invalidate()

- Store subscriptions (`useStore.subscribe`)
- DOM / window event listeners
- Tweens and timers (GSAP, `setTimeout`, `requestAnimationFrame`)
- Texture or data updates after async loading

## Continuous animation in demand mode

`useFrame` only runs on frames that are rendered. To keep animating, call `invalidate()` from inside it until the animation is done:

```jsx
useFrame((state, delta) => {
  ref.current.position.lerp(target, 1 - Math.pow(0.001, delta));
  if (ref.current.position.distanceTo(target) > 0.001) state.invalidate();
});
```
