# canvas-gl-config

---

title: Configure WebGL context via gl prop.
impact: HIGH

---

## Configure WebGL context

```jsx
<Canvas
  gl={{
    antialias: true,
    alpha: false,
    powerPreference: 'high-performance',
    stencil: false,
    depth: true,
  }}
  // Pixel ratio
  dpr={[1, 2]} // min 1, max 2
>
```
