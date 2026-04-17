# leva-basic

---

title: Basic Leva usage
impact: LOW

---

```jsx
import { useControls } from "leva";

function ControlledMesh() {
  const { position, color, wireframe } = useControls({
    position: { value: [0, 0, 0], step: 0.1 },
    color: "#ff0000",
    wireframe: false,
  });

  return (
    <mesh position={position}>
      <boxGeometry />
      <meshStandardMaterial color={color} wireframe={wireframe} />
    </mesh>
  );
}
```
