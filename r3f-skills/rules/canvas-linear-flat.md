# canvas-linear-flat

---

title: Use linear/flat for correct colors output.
impact: HIGH

---

```jsx
// For physically correct lighting (sRGB workflow)
<Canvas linear flat>
  {/* Scene renders in linear color space */}
  {/* Apply tonemapping in post-processing */}
</Canvas>

// linear: Uses LinearSRGBColorSpace for textures
// flat: Disables automatic tonemapping
```
