# physics-setup

---

title: Basic physics setup with Rapier.
impact: LOW-MEDIUM

---

```jsx
import { Physics, RigidBody } from "@react-three/rapier";

function Scene() {
  return (
    <Physics gravity={[0, -9.81, 0]} debug>
      {/* Dynamic body */}
      <RigidBody>
        <mesh>
          <boxGeometry />
          <meshStandardMaterial />
        </mesh>
      </RigidBody>

      {/* Static ground */}
      <RigidBody type="fixed">
        <mesh position={[0, -2, 0]}>
          <boxGeometry args={[10, 0.5, 10]} />
          <meshStandardMaterial />
        </mesh>
      </RigidBody>
    </Physics>
  );
}
```
