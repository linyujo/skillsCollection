# frame-priority

---

title: Use priority parameter for execution order.
impact: CRITICAL

---

Lower numbers run first. Default is 0.

## Example

```jsx
// Physics runs first, then animation, then camera
function Physics() {
  useFrame(() => {
    world.step();
  }, -100); // Runs first
}

function Animation() {
  useFrame(() => {
    updateAnimations();
  }, 0); // Default priority
}

function CameraFollow() {
  useFrame(() => {
    camera.lookAt(target);
  }, 100); // Runs last
}
```
