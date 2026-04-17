# drei-text

---

title: Use Text for 3D text (troika-three-text).
impact: MEDIUM-HIGH

---

## 2D text in 3D space (SDF, very performant)

```jsx
import { Text } from "@react-three/drei";

<Text
  color="black"
  fontSize={1}
  maxWidth={10}
  lineHeight={1}
  letterSpacing={0}
  textAlign="center"
  font="/fonts/Inter-Bold.woff"
  anchorX="center"
  anchorY="middle"
>
  Hello World
</Text>;
```

## 3D extruded text

```jsx
import { Text } from "@react-three/drei";

<Text3D
  font="/fonts/helvetiker_regular.typeface.json"
  size={1}
  height={0.2}
  bevelEnabled
  bevelSize={0.02}
>
  Hello
  <meshStandardMaterial color="orange" />
</Text3D>;
```
