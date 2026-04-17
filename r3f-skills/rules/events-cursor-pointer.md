# events-cursor-pointer

---

title: Change cursor on hover.
impact: MEDIUM

---

## Good Example

```jsx
function HoverCursor() {
  const [hovered, setHovered] = useState(false);

  // Change cursor
  useEffect(() => {
    document.body.style.cursor = hovered ? "pointer" : "auto";
    return () => {
      document.body.style.cursor = "auto";
    };
  }, [hovered]);

  return (
    <mesh
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
    >
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```

## Good Example 2 - use useCursor from Drei

```jsx
import { useCursor } from "@react-three/drei";

function HoverCursorDrei() {
  const [hovered, setHovered] = useState(false);
  useCursor(hovered);

  return (
    <mesh
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
    >
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```
