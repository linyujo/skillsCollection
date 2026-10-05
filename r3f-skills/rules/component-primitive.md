---
name: component-primitive
title: "Clone loaded models correctly before reusing them."
impact: HIGH
---

# component-primitive

`<primitive object={obj} />` mounts an existing Three.js object as-is. Two traps:

1. A Three.js object can only have **one parent**. Mounting the same object twice moves it; only the last one is visible.
2. `useGLTF` returns a **cached** scene. Every component that loads the same URL gets the same object.

## Bad Example

```jsx
// BAD - Same cached scene mounted 3 times → only one tree is visible
function Tree({ position }) {
  const { scene } = useGLTF("/tree.glb");
  return <primitive object={scene} position={position} />;
}

// BAD - Clones on every render, and breaks skinned meshes
function Character() {
  const { scene } = useGLTF("/character.glb");
  return <primitive object={scene.clone()} />;
}
```

`scene.clone()` in render creates a new object graph on every re-render (and `<primitive>` reconstructs when `object` changes). For skinned meshes, `Object3D.clone()` keeps the clone's bones bound to the original skeleton, so the copy doesn't animate correctly.

## Good Example 1 - SkeletonUtils.clone in useMemo

```jsx
import { useMemo } from "react";
import { useGLTF } from "@react-three/drei";
import * as SkeletonUtils from "three/addons/utils/SkeletonUtils.js";

function Character({ position }) {
  const { scene } = useGLTF("/character.glb");
  // Clone once per component; SkeletonUtils.clone rebinds bones correctly
  const clone = useMemo(() => SkeletonUtils.clone(scene), [scene]);
  return <primitive object={clone} position={position} />;
}
```

`SkeletonUtils.clone` also works for models without bones, so it is a safe default.

## Good Example 2 - drei `<Clone>`

```jsx
import { Clone, useGLTF } from "@react-three/drei";

function Tree({ position }) {
  const { scene } = useGLTF("/tree.glb");
  return <Clone object={scene} position={position} />;
}
```

## Notes

- Clones share geometries and materials with the cached original. Changing `material.color` on one clone changes all of them; clone the material too if each copy needs its own.
- For many copies of the same static mesh, prefer instancing over cloning.
