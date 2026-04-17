# physics-colliders

---

title: Use appropriate colliders.
impact: LOW-MEDIUM

---

## Colliders

```jsx
// Auto-collider from mesh
<RigidBody colliders="hull"> {/* convex hull */}
  <mesh />
</RigidBody>

<RigidBody colliders="cuboid"> {/* box */}
  <mesh />
</RigidBody>

<RigidBody colliders="ball"> {/* sphere */}
  <mesh />
</RigidBody>

<RigidBody colliders="trimesh"> {/* exact mesh shape (expensive) */}
  <mesh />
</RigidBody>

// Manual colliders
import { CuboidCollider, BallCollider, CapsuleCollider } from '@react-three/rapier';

<RigidBody colliders={false}>
  <CuboidCollider args={[0.5, 0.5, 0.5]} />
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</RigidBody>
```
