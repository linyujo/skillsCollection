---
name: frame-delta-time
title: "Always use delta for frame-rate independent animation."
impact: CRITICAL
---

# frame-delta-time

## Bad Example

```jsx
// BAD - Speed depends on frame rate (2x faster on a 120Hz screen)
useFrame(() => {
  ref.current.rotation.y += 0.01;
});
```

## Good Example

```jsx
// GOOD - Units per second, same speed on every device
useFrame((_, delta) => {
  ref.current.rotation.y += 1 * delta;
});
```

## Good Example - Frame-rate independent lerp

`lerp(target, 0.1)` has the same problem: it converges faster at higher frame rates. Derive the factor from `delta`:

```jsx
useFrame((_, delta) => {
  const t = 1 - Math.pow(0.001, delta); // 0.001 = fraction left after 1 second
  ref.current.position.lerp(target, t);
});

// Same idea for scalars
useFrame((_, delta) => {
  ref.current.rotation.y = THREE.MathUtils.damp(ref.current.rotation.y, targetY, 4, delta);
});
```

## Elapsed time and THREE.Clock

- `state.clock.elapsedTime` is fine for time-based effects such as `Math.sin(state.clock.elapsedTime)`.
- three r183 deprecated `THREE.Clock`. R3F v9 still creates one for `state.clock`, so a console warning `Clock: This module has been deprecated` comes from R3F itself, not from your code. It can be ignored.
- Don't create your own `new THREE.Clock()`. If you need an independent timer, use `THREE.Timer`.
