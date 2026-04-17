# drei-bounds

---

title: Use Bounds to fit camera to objects.
impact: MEDIUM-HIGH

---

```jsx
import { Bounds, useBounds } from "@react-three/drei";

function FitToView() {
  return (
    <Bounds fit clip observe margin={1.2}>
      <Model />
    </Bounds>
  );
}

// Manual control
function ManualBounds() {
  const bounds = useBounds();

  return (
    <mesh onClick={() => bounds.refresh().fit()}>
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```
