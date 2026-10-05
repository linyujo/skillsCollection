# frame-conditional-subscription

---

title: Disable useFrame when not needed.
impact: CRITICAL

---

`useFrame` subscribes on mount and unsubscribes on unmount. There is no argument that turns a mounted `useFrame` off.

Passing `null` (or anything else) as the priority does **not** skip the subscription: the callback still runs every frame.

## Bad Example

```jsx
// BAD - null does not unsubscribe, the callback still runs every frame
function Spinner({ active }) {
  const ref = useRef();
  useFrame(
    (_, delta) => {
      ref.current.rotation.y += delta;
    },
    active ? 0 : null,
  );
  return <mesh ref={ref} />;
}
```

## Good Example 1 - Unmount to really unsubscribe

Put the `useFrame` in its own component and mount it only while it is needed.

```jsx
// GOOD - No subscription at all while inactive
function Spinner({ active }) {
  const ref = useRef();
  return (
    <>
      <mesh ref={ref} />
      {active && <SpinAnimator target={ref} />}
    </>
  );
}

function SpinAnimator({ target }) {
  useFrame((_, delta) => {
    target.current.rotation.y += delta;
  });
  return null;
}
```

Keep the mesh mounted and only toggle the animator, so the Three.js object is not rebuilt.

## Good Example 2 - Pause with an early return

For animations that pause and resume often, keep the subscription and return early. Gate it with a ref so toggling does not re-render.

```jsx
// GOOD - ~a few ns per frame while idle, no re-render to toggle
function OneShotAnimation({ duration = 1 }) {
  const ref = useRef();
  const playing = useRef(false);
  const elapsed = useRef(0);

  const start = () => {
    elapsed.current = 0;
    playing.current = true;
  };

  useFrame((_, delta) => {
    if (!playing.current) return;
    elapsed.current += delta;
    ref.current.position.y = Math.sin((elapsed.current / duration) * Math.PI);
    if (elapsed.current >= duration) playing.current = false;
  });

  return <mesh ref={ref} onClick={start} />;
}
```
