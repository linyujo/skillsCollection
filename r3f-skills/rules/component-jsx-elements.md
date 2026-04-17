# component-jsx-elements

---

title: R3F automatically creates Three.js objects from lowercase JSX elements.
impact: HIGH

---

## JSX elements map to THREE constructors

| JSX Element              | THREE Constructor            |
| ------------------------ | ---------------------------- |
| `<mesh>`                 | `THREE.Mesh`                 |
| `<boxGeometry>`          | `THREE.BoxGeometry`          |
| `<meshStandardMaterial>` | `THREE.MeshStandardMaterial` |
| `<ambientLight>`         | `THREE.AmbientLight`         |
| `<group>`                | `THREE.Group`                |

## Constructor arguments via args prop

```jsx
// BoxGeometry(width, height, depth)
<boxGeometry args={[2, 1, 0.5]} />

// MeshStandardMaterial(options)
<meshStandardMaterial args={[{ color: "hotpink" }]} />

// DirectionalLight(color, intensity)
<directionalLight args={["white", 1]} />
```
