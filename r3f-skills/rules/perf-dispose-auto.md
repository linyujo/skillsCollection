---
name: perf-dispose-auto
title: "Understand what R3F disposes, and what it doesn't."
impact: CRITICAL
impactDescription: "R3F frees GPU resources it created from JSX, but never the ones you created yourself. Shared JSX resources can be freed too early; resources created with new / useMemo leak."
---

# perf-dispose-auto

## What R3F actually does on unmount (v9)

1. It calls `.dispose()` on the **element's own object** only, if that object has a `dispose` method, during browser idle time.
2. It walks down the **JSX children** and does the same for each of them.
3. `Mesh`, `Group` and other `Object3D`s have no `dispose` method. A geometry or material passed as a **prop** (`geometry={geo}`, `material={mat}`) is not a JSX child, so it is **not** disposed.
4. `<primitive object={...} />` is **never** disposed (neither is a `Scene`). Its JSX children still are.
5. `dispose={null}` on an element protects it **and its whole subtree**.

```jsx
function MyMesh() {
  return (
    <mesh>
      <boxGeometry /> {/* JSX child → disposed on unmount */}
      <meshStandardMaterial /> {/* JSX child → disposed on unmount */}
    </mesh>
  );
}
```

## Trap 1 - A JSX resource shared through a ref gets disposed

```jsx
// BAD - The material is declared as a JSX child of the panel,
// then reused by another mesh. Unmounting the panel disposes it for everyone.
function Panel({ onMaterial }) {
  return (
    <mesh>
      <planeGeometry />
      <meshStandardMaterial ref={(m) => m && onMaterial(m)} color="orange" />
    </mesh>
  );
}

function Scene({ showPanel }) {
  const [material, setMaterial] = useState(null);
  return (
    <>
      {showPanel && <Panel onMaterial={setMaterial} />}
      {material && (
        <mesh material={material}>
          <boxGeometry />
        </mesh>
      )}
    </>
  );
}
```

When `showPanel` becomes `false`, R3F disposes the material while the box still uses it. three silently rebuilds the GPU program on the next render, so every unmount of the panel causes a shader recompile hitch. If the shared resource is a render target, its rendered content is lost.

```jsx
// GOOD (option 1) - Opt the shared material out of auto-dispose
<meshStandardMaterial ref={(m) => m && onMaterial(m)} color="orange" dispose={null} />
```

```jsx
// GOOD (option 2) - Own the shared resource in the common parent
// and pass it as a prop: props are never disposed (see Trap 2 for cleanup)
function Scene() {
  const material = useMemo(() => new THREE.MeshStandardMaterial({ color: "orange" }), []);
  useEffect(() => () => material.dispose(), [material]);
  return (
    <>
      <mesh material={material}><planeGeometry /></mesh>
      <mesh material={material}><boxGeometry /></mesh>
    </>
  );
}
```

## Trap 2 - Resources you create yourself leak

Anything created with `new` (in `useMemo`, `useState`, module scope, or a loader you call manually) is invisible to R3F's disposal. Geometries, materials, textures and render targets created this way stay in GPU memory after the component unmounts.

```jsx
// BAD - New GPU resources on every mount, never freed
function Blob() {
  const geometry = useMemo(() => new THREE.IcosahedronGeometry(1, 64), []);
  const target = useMemo(() => new THREE.WebGLRenderTarget(1024, 1024), []);
  return <mesh geometry={geometry} />;
}
```

```jsx
// GOOD - Dispose in the effect cleanup
function Blob() {
  const geometry = useMemo(() => new THREE.IcosahedronGeometry(1, 64), []);
  const target = useMemo(() => new THREE.WebGLRenderTarget(1024, 1024), []);

  useEffect(
    () => () => {
      geometry.dispose();
      target.dispose();
    },
    [geometry, target],
  );

  return <mesh geometry={geometry} />;
}
```

## Notes

- Loader caches (`useGLTF`, `useTexture`) keep their resources for reuse. Don't dispose them manually unless you also clear the cache (`useGLTF.clear(url)`).
- Check for leaks with `gl.info.memory` (`geometries`, `textures`): the numbers should return to their previous values after a component unmounts.
