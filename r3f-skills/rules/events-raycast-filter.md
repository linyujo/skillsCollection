# events-raycast-filter

---

title: Filter raycasting with raycast prop or layers.
impact: MEDIUM

---

```jsx
// Disable raycasting entirely
<mesh raycast={() => null}>
  <boxGeometry />
  <meshStandardMaterial />
</mesh>;

// Use layers for selective raycasting
function SelectiveRaycast() {
  const meshRef = useRef();

  useEffect(() => {
    meshRef.current.layers.set(1); // Only layer 1
  }, []);

  return <mesh ref={meshRef} />;
}
```
