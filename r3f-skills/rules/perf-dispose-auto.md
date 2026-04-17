# perf-dispose-auto

---

title: Understand R3F auto-dispose behavior.
impact: CRITICAL
impactDescription: R3F automatically disposes geometries, materials, and textures when components unmount. Understand when to disable.

---

## Default Behavior Example

```jsx
// Auto-dispose is ON by default (good!)

function MyMesh() {
  return (
    <mesh>
      <boxGeometry /> {/* Auto-disposed on unmount */}
      <meshStandardMaterial /> {/* Auto-disposed on unmount */}
    </mesh>
  );
}
```

## When to Disable Auto-Dispose

- When sharing resources between components
- Disable on primitive for external objects

## How to Disable Auto-Dispose

```jsx
//  When sharing resources between components
const sharedGeometry = new THREE.BoxGeometry();

function ReusedMesh() {
  return (
    <mesh geometry={sharedGeometry}>
      <meshStandardMaterial dispose={null} /> {/* Manual disposal */}
    </mesh>
  );
}
```

```jsx
// Disable on primitive for external objects

function ImportedModel({ object }) {
  return <primitive object={object} dispose={null} />;
}
```
