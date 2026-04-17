# frame-destructure-state

---

title: Destructure only what you need from state.
impact: CRITICAL

---

## Bad Example

```jsx
// BAD - Get the whole state object

function BadAnimation({ mesh }) {
  useFrame((state) => {
    const { camera, scene, clock } = state;
    mesh.rotation.y = clock.elapsedTime; // Only clock is needed
  });
}
```

## Good Example

```jsx
// GOOD - Destructuring only what's needed

function GoodAnimation({ mesh }) {
  useFrame(({ clock }) => {
    // Only get what you need
    mesh.rotation.y = clock.elapsedTime;
  });
}
```

## useFrame state object contents

- gl
- scene
- camera
- raycaster
- pointer
- mouse
- clock
- viewport
- size
- set
- get
- invalidate
- advance
- events
