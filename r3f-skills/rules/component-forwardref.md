# component-forwardref

---

title: Use forwardRef for reusable components that need refs.
impact: HIGH

---

## For reusable components

```jsx
// reusable components
const Box = forwardRef(function Box({ color = "orange", ...props }, ref) {
  return (
    <mesh ref={ref} {...props}>
      <boxGeometry />
      <meshStandardMaterial color={color} />
    </mesh>
  );
});

// Usage
function Scene() {
  const boxRef = useRef();

  useFrame(() => {
    boxRef.current.rotation.x += 0.01;
  });

  return <Box ref={boxRef} position={[0, 1, 0]} color="blue" />;
}
```
