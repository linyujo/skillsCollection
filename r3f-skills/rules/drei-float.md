# drei-float

---

title: Use Float for floating animation.
impact: MEDIUM-HIGH

---

```jsx
import { Float } from "@react-three/drei";

<Float
  speed={1}
  rotationIntensity={1}
  floatIntensity={1}
  floatingRange={[-0.1, 0.1]}
>
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</Float>;
```
