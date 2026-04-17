# events-pointer-events

---

title: Use pointer events on meshes.
impact: MEDIUM

---

```jsx
function InteractiveMesh() {
  const [hovered, setHovered] = useState(false);

  return (
    <mesh
      onClick={(e) => {
        e.stopPropagation(); // Prevent event bubbling
        console.log("Clicked!", e.point); // World position
      }}
      onPointerOver={(e) => setHovered(true)}
      onPointerOut={(e) => setHovered(false)}
      onPointerMove={(e) => console.log(e.point)}
      onPointerDown={(e) => console.log("Down")}
      onPointerUp={(e) => console.log("Up")}
    >
      <boxGeometry />
      <meshStandardMaterial color={hovered ? "hotpink" : "orange"} />
    </mesh>
  );
}
```
