# frame-conditional-subscription

---

title: Disable useFrame when not needed.
impact: CRITICAL

---

## Bad Example

```jsx
// BAD - Always running

function BadAnimation() {
  useFrame((state, delta) => {
    ref.current.rotation.y += delta * 2;
  });
}
```

## Good Example

```jsx
// GOOD - Active only when needed

function GoodAnimation({ active }) {
  useFrame(
    () => {
      // Animation logic
    },
    active ? 0 : null,
  ); // null disables the subscription
}
```

## Good Example 2

```jsx
// GOOD - Alternative with early return

function ConditionalAnimation({ paused }) {
  useFrame((state, delta) => {
    if (paused) return;
    // Animation logic
  });
}
```
