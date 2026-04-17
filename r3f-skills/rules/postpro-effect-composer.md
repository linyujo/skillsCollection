# postpro-effect-composer

---

title: Use EffectComposer from @react-three/postprocessing.
impact: MEDIUM

---

```jsx
import { EffectComposer, Bloom, Vignette } from "@react-three/postprocessing";

function Scene() {
  return (
    <>
      <mesh>
        <boxGeometry />
        <meshStandardMaterial emissive="orange" emissiveIntensity={2} />
      </mesh>

      <EffectComposer>
        <Bloom
          luminanceThreshold={0.2}
          luminanceSmoothing={0.9}
          intensity={1}
        />
        <Vignette eskil={false} offset={0.1} darkness={1.1} />
      </EffectComposer>
    </>
  );
}
```
