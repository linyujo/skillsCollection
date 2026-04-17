# events-stop-propagation

---

title: Use stopPropagation to prevent event bubbling.
impact: MEDIUM

---

```jsx
// Events bubble through the scene graph
function Parent() {
  return (
    <group onClick={() => console.log("Parent clicked")}>
      <Child />
    </group>
  );
}

function Child() {
  return (
    <mesh
      onClick={(e) => {
        e.stopPropagation(); // Parent won't receive click
        console.log("Child clicked");
      }}
    >
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```
