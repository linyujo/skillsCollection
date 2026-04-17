# physics-body-types

---

title: Understand RigidBody types.
impact: LOW-MEDIUM

---

## RigidBody Types

```jsx
// Dynamic - Affected by forces and collisions
<RigidBody type="dynamic">
  <mesh />
</RigidBody>

// Fixed - Immovable, infinite mass
<RigidBody type="fixed">
  <mesh />
</RigidBody>

// Kinematic - Moved programmatically, not by physics
<RigidBody type="kinematicPosition">
  <mesh />
</RigidBody>

// Kinematic velocity-based
<RigidBody type="kinematicVelocity">
  <mesh />
</RigidBody>
```
