# physics-performance

---

title: Optimize physics performance.
impact: LOW-MEDIUM

---

## Physics API

```jsx
<Physics
  gravity={[0, -9.81, 0]}
  timeStep="vary" // or fixed like 1/60
  updatePriority={-50} // Run before rendering
  interpolate={true} // Smooth motion between physics steps
>
  {/* Use simple colliders instead of trimesh */}
  <RigidBody colliders="cuboid">
    <mesh />
  </RigidBody>

  {/* Disable collision detection when not needed */}
  <RigidBody sensor>
    <CuboidCollider args={[5, 5, 5]} />
  </RigidBody>
</Physics>
```
