# physics-events

---

title: Handle collision events.
impact: LOW-MEDIUM

---

## Collision Events

```jsx
<RigidBody
  onCollisionEnter={({ manifold, target, other }) => {
    console.log("Collision with", other.rigidBodyObject.name);
    console.log("Contact point", manifold.solverContactPoint(0));
  }}
  onCollisionExit={({ target, other }) => {
    console.log("Collision ended with", other.rigidBodyObject.name);
  }}
  onIntersectionEnter={({ target, other }) => {
    // For sensor colliders
    console.log("Entered trigger zone");
  }}
>
  <mesh name="player">
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</RigidBody>
```
