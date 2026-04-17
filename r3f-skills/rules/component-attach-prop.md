# component-attach-prop

---

title: Use attach for non-standard parent properties.
impact: HIGH

---

## Geometry and material auto-attach

```jsx
<mesh>
  <boxGeometry /> {/* attach="geometry" (automatic) */}
  <meshStandardMaterial /> {/* attach="material" (automatic) */}
</mesh>
```

## Explicit attach for other properties

```jsx
<mesh>
  <boxGeometry attach="geometry" />
  <meshStandardMaterial attach="material" />
</mesh>
```

## Array attachment with attach function

```jsx
<mesh>
  <meshStandardMaterial
    attach={(parent, self) => {
      parent.material = [self]; // or parent.material.push(self)
      return () => {
        /* cleanup */
      };
    }}
  />
</mesh>
```

## Shadow map attachment

```jsx
<directionalLight>
  <orthographicCamera attach="shadow-camera" args={[-10, 10, 10, -10]} />
</directionalLight>
```
