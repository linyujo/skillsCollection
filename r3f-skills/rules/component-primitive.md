# component-primitive

---

title: Use primitive for existing Three.js objects.
impact: HIGH

---

## For objects created outside React

```jsx
const mesh = new THREE.Mesh(geometry, material);

function ExternalObject() {
  return <primitive object={mesh} position={[0, 1, 0]} />;
}
```

## For loaded models

```jsx
function Model() {
  const { scene } = useGLTF("/model.glb");
  return <primitive object={scene} />;
}
```

## Clone if reusing

```jsx
function ReusableModel() {
  const { scene } = useGLTF("/model.glb");
  return <primitive object={scene.clone()} />;
}
```
