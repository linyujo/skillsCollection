# drei-instances

---

title: Use Instances for rendering many copies of the same object.
impact: MEDIUM-HIGH

---

```jsx
import { Instances, Instance } from "@react-three/drei";

function Particles({ count = 1000 }) {
  return (
    <Instances limit={count} range={count}>
      <boxGeometry args={[0.1, 0.1, 0.1]} />
      <meshStandardMaterial />

      {Array.from({ length: count }, (_, i) => (
        <Instance
          key={i}
          position={[
            Math.random() * 10,
            Math.random() * 10,
            Math.random() * 10,
          ]}
          rotation={[Math.random(), Math.random(), 0]}
          color={`hsl(${Math.random() * 360}, 100%, 50%)`}
        />
      ))}
    </Instances>
  );
}
```
