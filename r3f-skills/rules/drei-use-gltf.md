# drei-use-gltf

---

title: Use useGLTF for model loading with preloading.
impact: MEDIUM-HIGH

---

## Why It Matters

- Suspense integration (automatic loading states)
- Caching (same model loaded once)
- Draco compression support
- Preloading capability

## Basic Example

```jsx
import { useGLTF } from "@react-three/drei";

function Model() {
  const { scene, nodes, materials } = useGLTF("/model.glb");
  return <primitive object={scene} />;
}
```

## Preloading

Critical for UX

```jsx
import { useGLTF } from "@react-three/drei";

function Model() {
  const { scene } = useGLTF("/model.glb");
  return <primitive object={scene} />;
}

// Preload at module level - starts loading immediately
useGLTF.preload("/model.glb");

// Or preload multiple models
useGLTF.preload(["/model1.glb", "/model2.glb", "/model3.glb"]);
```

## Accessing Nodes and Materials

```jsx
function Character() {
  const { nodes, materials } = useGLTF("/character.glb");

  return (
    <group>
      <mesh geometry={nodes.Body.geometry} material={materials.Skin} />
      <mesh geometry={nodes.Clothes.geometry} material={materials.Fabric} />
    </group>
  );
}
```

## Clone for Multiple Instances

```jsx
function Tree({ position }) {
  const { scene } = useGLTF("/tree.glb");

  // Clone to avoid sharing state between instances
  return <primitive object={scene.clone()} position={position} />;
}

function Forest() {
  return (
    <>
      <Tree position={[0, 0, 0]} />
      <Tree position={[5, 0, 0]} />
      <Tree position={[10, 0, 0]} />
    </>
  );
}
```

## TypeScript Types

```jsx
import { useGLTF } from '@react-three/drei';
import { GLTF } from 'three-stdlib';

type GLTFResult = GLTF & {
  nodes: {
    Body: THREE.Mesh;
    Head: THREE.Mesh;
  };
  materials: {
    Skin: THREE.MeshStandardMaterial;
  };
};

function Model() {
  const { nodes, materials } = useGLTF('/model.glb') as GLTFResult;
  // Now nodes.Body and materials.Skin are typed
}
```
