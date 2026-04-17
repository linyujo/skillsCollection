# drei-use-helper

---

title: Use useHelper for debug visualization.
impact: MEDIUM-HIGH

---

```jsx
import { useHelper } from "@react-three/drei";
import { DirectionalLightHelper, BoxHelper } from "three";

function DebugLight() {
  const lightRef = useRef();
  useHelper(lightRef, DirectionalLightHelper, 1, "red");

  return <directionalLight ref={lightRef} />;
}

function DebugMesh() {
  const meshRef = useRef();
  useHelper(meshRef, BoxHelper, "blue");

  return (
    <mesh ref={meshRef}>
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```
