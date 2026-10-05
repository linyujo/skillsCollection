# canvas-linear-flat

---

title: Don't override R3F's color management.
impact: HIGH

---

three r152 rewrote color management. Old tutorials (and much training data) still use the removed API.

## Old API → current API

| Removed (three < r152)                    | Current                                     |
| ----------------------------------------- | ------------------------------------------- |
| `gl.outputEncoding = THREE.sRGBEncoding`  | `gl.outputColorSpace = THREE.SRGBColorSpace` |
| `texture.encoding = THREE.sRGBEncoding`   | `texture.colorSpace = THREE.SRGBColorSpace` |
| `THREE.LinearEncoding`                    | `THREE.LinearSRGBColorSpace`                |
| `gl.physicallyCorrectLights = true`       | Removed: physically correct lighting is always on |

## R3F defaults are already correct

Without any props, `<Canvas>` sets:

- `gl.outputColorSpace = THREE.SRGBColorSpace`
- `gl.toneMapping = THREE.ACESFilmicToneMapping`
- `THREE.ColorManagement.enabled = true`

## Bad Example

```jsx
// BAD - Copied from an old tutorial
<Canvas
  linear
  flat
  onCreated={({ gl }) => {
    gl.outputEncoding = THREE.sRGBEncoding; // Removed API
  }}
>
```

## What the props actually change

| Prop     | Effect                                                                                  | Use it when                                                        |
| -------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `linear` | `gl.outputColorSpace = LinearSRGBColorSpace`, and turns off the automatic sRGB tagging of textures (below) | Output goes to something that applies its own sRGB conversion      |
| `flat`   | `gl.toneMapping = NoToneMapping`                                                        | Tone mapping is done elsewhere (e.g. a `ToneMapping` post effect), or UI colors must match exactly |
| `legacy` | `THREE.ColorManagement.enabled = false`                                                 | Almost never; only to reproduce pre-r152 colors                    |

Explicit `gl={{ outputColorSpace, toneMapping }}` values take precedence over `linear` / `flat`.

## Texture color space

When a texture is passed through JSX to `map`, `emissiveMap`, `sheenColorMap`, `specularColorMap` or `envMap`, R3F sets `texture.colorSpace = SRGBColorSpace` for you (only for 8-bit RGBA textures, and only without `linear`).

Set it yourself when R3F can't see the assignment:

```jsx
// Assigned imperatively or through a custom shader uniform → set it manually
const tex = useTexture("/albedo.jpg");
tex.colorSpace = THREE.SRGBColorSpace;
material.map = tex;

// Data textures (normalMap, roughnessMap, ...) must stay linear: don't tag them sRGB
```
