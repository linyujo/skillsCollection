# component-dispose-null

---

title: Set dispose={null} on shared or external resources.
impact: HIGH

---

## Shared geometry across components

```jsx
const sharedGeo = new THREE.SphereGeometry(1, 32, 32);

function SharedSphere({ position }) {
  return (
    <mesh position={position} geometry={sharedGeo}>
      <meshStandardMaterial />
    </mesh>
  );
}
```

## External/loaded objects

```jsx
function LoadedModel({ model }) {
  return <primitive object={model} dispose={null} />;
}
```
