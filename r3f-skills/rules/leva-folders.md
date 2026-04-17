# leva-folders

---

title: Organize controls with folders.
impact: LOW

---

```jsx
const { ambient, directional } = useControls("Lighting", {
  ambient: { value: 0.5, min: 0, max: 1, step: 0.1 },
  directional: { value: 1, min: 0, max: 2, step: 0.1 },
});

// Nested folders
const materialProps = useControls("Material", {
  color: "#ffffff",

  "PBR Properties": folder({
    metalness: { value: 0.5, min: 0, max: 1 },
    roughness: { value: 0.5, min: 0, max: 1 },
  }),
});
```
