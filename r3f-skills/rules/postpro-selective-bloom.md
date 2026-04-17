# postpro-selective-bloom

---

title: Use SelectiveBloom for optimized glow.
impact: MEDIUM

---

```jsx
import { SelectiveBloom } from "@react-three/postprocessing";

function Scene() {
  const glowRef = useRef();

  return (
    <>
      {/* This mesh will glow */}
      <mesh ref={glowRef}>
        <sphereGeometry />
        <meshStandardMaterial emissive="orange" />
      </mesh>

      {/* This mesh won't glow */}
      <mesh position={[2, 0, 0]}>
        <boxGeometry />
        <meshStandardMaterial color="blue" />
      </mesh>

      <EffectComposer>
        <SelectiveBloom
          selection={glowRef}
          intensity={2}
          luminanceThreshold={0.1}
        />
      </EffectComposer>
    </>
  );
}
```
