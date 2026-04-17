# drei-center

---

title: Use Center to center objects.
impact: MEDIUM-HIGH

---

```jsx
import { Center } from "@react-three/drei";

function CenteredModel() {
  return (
    <Center top>
      {" "}
      {/* Align to top */}
      <Model />
    </Center>
  );
}
```

## Options

- top, bottom, left, right, front, back
- precise
