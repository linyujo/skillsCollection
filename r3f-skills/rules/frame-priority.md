# frame-priority

---

title: Positive priority takes over rendering.
impact: CRITICAL
impactDescription: Any useFrame with priority > 0 switches off R3F's automatic render. If that callback doesn't render, the screen stops updating.

---

`useFrame(callback, priority)` sorts callbacks from low to high. Default is `0`.

But a **positive** priority is not just "run later": as long as at least one subscriber has `priority > 0`, R3F skips its own `gl.render(scene, camera)` and expects you to render.

R3F's automatic render always runs **after** every callback, so ordering never needs a positive number.

## Bad Example

```jsx
// BAD - Wanted "camera runs last", got a frozen screen
function CameraFollow({ target }) {
  useFrame(({ camera }) => {
    camera.lookAt(target);
  }, 100); // priority > 0 → R3F stops rendering, nothing calls gl.render
}
```

## Good Example - Ordering with negative numbers and 0

```jsx
// GOOD - Physics → animation → camera, R3F still renders after all of them
function Physics() {
  useFrame(() => world.step(), -2);
}

function Animation() {
  useFrame(() => updateAnimations(), -1);
}

function CameraFollow({ target }) {
  useFrame(({ camera }) => camera.lookAt(target), 0);
}
```

## Good Example - Positive priority that renders by itself

```jsx
// GOOD - Custom post-processing: this callback replaces R3F's render
function Composer() {
  const gl = useThree((s) => s.gl);
  const scene = useThree((s) => s.scene);
  const camera = useThree((s) => s.camera);
  const composer = useMemo(() => {
    const c = new EffectComposer(gl);
    c.addPass(new RenderPass(scene, camera));
    return c;
  }, [gl, scene, camera]);

  useFrame((_, delta) => {
    composer.render(delta); // Must render, R3F won't
  }, 1);

  return null;
}
```

## When a positive priority is actually needed

Only when you replace or extend the final render to the screen:

1. **Post-processing** - `composer.render()` must replace R3F's render, otherwise R3F renders the raw scene again on top.
2. **HUD / overlay scene** - render the main scene, set `gl.autoClear = false`, `gl.clearDepth()`, then render a second scene on top.
3. **Split screen / picture-in-picture** - multiple `setViewport` / `setScissor` renders in one canvas.

Not needed for:

- Execution order only - use negative numbers and `0`.
- Render-to-texture - render into a render target, restore it, and let R3F render the main scene as usual.

## Libraries that already use a positive priority

- `@react-three/postprocessing` `<EffectComposer>` - `renderPriority = 1`
- `@react-three/drei` `<Hud>` - `renderPriority = 1` (layer 1 renders the main scene, higher layers overlay)
- `@react-three/drei` `<GizmoHelper>`, `<Fisheye>` - also take over rendering

If one of these is mounted, adding your own positive-priority render callback means two callbacks render the frame. Coordinate them (one renders the scene, the other only overlays), or drop yours.
