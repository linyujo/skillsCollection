# drei-orbit-controls

---

title: Use OrbitControls from Drei (not manual extend).
impact: MEDIUM-HIGH

---

```jsx
import { OrbitControls } from "@react-three/drei";

function Scene() {
  return (
    <>
      <OrbitControls
        enableDamping
        dampingFactor={0.05}
        minDistance={2}
        maxDistance={50}
        maxPolarAngle={Math.PI / 2}
      />
      <mesh>
        <boxGeometry />
        <meshStandardMaterial />
      </mesh>
    </>
  );
}
```
