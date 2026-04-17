# loading-suspense

---

title: Wrap async components in Suspense.
impact: MEDIUM-HIGH

---

R3F integrates with React Suspense for loading states. Components using useGLTF, useTexture, or other async loaders will suspend and need a Suspense boundary with a fallback.

## Good Example Basic

```jsx
import { Suspense } from "react";
import { useGLTF } from "@react-three/drei";

function Model() {
  const { scene } = useGLTF("/model.glb");
  return <primitive object={scene} />;
}

function App() {
  return (
    <Canvas>
      <Suspense fallback={<LoadingFallback />}>
        <Model /> {/* Uses useGLTF internally */}
      </Suspense>
    </Canvas>
  );
}

function LoadingFallback() {
  return (
    <mesh>
      <boxGeometry />
      <meshBasicMaterial wireframe />
    </mesh>
  );
}
```

## Good Example Multiple Async Components

```jsx
function Scene() {
  return (
    <Suspense fallback={<Loader />}>
      <Environment preset="city" />
      <Model url="/character.glb" />
      <Ground />
    </Suspense>
  );
}
```

## Good Example Nested Suspense Boundaries

```jsx
function Scene() {
  return (
    <>
      {/* Environment loads first */}
      <Suspense fallback={null}>
        <Environment preset="sunset" />
      </Suspense>

      {/* Main content with visible loader */}
      <Suspense fallback={<Loader />}>
        <Character />
        <Props />
      </Suspense>

      {/* Background loads last, no blocking */}
      <Suspense fallback={null}>
        <BackgroundDetails />
      </Suspense>
    </>
  );
}
```
