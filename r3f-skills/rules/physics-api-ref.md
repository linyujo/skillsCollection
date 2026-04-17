# physics-api-ref

---

title: Use ref for physics API access.
impact: LOW-MEDIUM

---

## Physics API

```jsx
import { RigidBody } from "@react-three/rapier";

function Player() {
  const rigidBodyRef = useRef();

  const jump = () => {
    rigidBodyRef.current.applyImpulse({ x: 0, y: 10, z: 0 }, true);
  };

  const move = (direction) => {
    rigidBodyRef.current.setLinvel({
      x: direction.x * 5,
      y: 0,
      z: direction.z * 5,
    });
  };

  useFrame(() => {
    const position = rigidBodyRef.current.translation();
    const velocity = rigidBodyRef.current.linvel();
    // Use position and velocity
  });

  return (
    <RigidBody ref={rigidBodyRef}>
      <mesh>
        <capsuleGeometry args={[0.5, 1]} />
        <meshStandardMaterial />
      </mesh>
    </RigidBody>
  );
}
```
