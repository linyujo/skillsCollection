---
name: component-args-reconstruct
title: "Changing args rebuilds the whole object."
impact: HIGH
impactDescription: "When any args element changes, R3F disposes the old Three.js object and constructs a new one. GPU data is re-uploaded and everything done to the old object through its ref is lost."
---

# component-args-reconstruct

`args` are constructor arguments. Three.js can't apply new constructor arguments to an existing object, so R3F compares `args` element by element (`!==`) on every render and, if anything differs (or the length changes), it:

1. Detaches and **disposes** the old object
2. Calls `new Target(...args)` again
3. Re-applies the JSX props and re-attaches the children
4. Points the ref at the new object

Anything that was done to the old object imperatively (e.g. `geometry.translate()`, `computeVertexNormals()`, attribute edits in an effect, values set in `useFrame`) is gone. Code that kept the old object (in a closure, a store, a `useMemo`) now holds a disposed object.

`<primitive object={...} />` behaves the same way when `object` changes.

## Bad Example 1 - Animating through args

```jsx
// BAD - Every size change disposes and rebuilds the geometry
function GrowingBox() {
  const [size, setSize] = useState(1);
  return (
    <mesh onClick={() => setSize((s) => s + 0.1)}>
      <boxGeometry args={[size, size, size]} />
      <meshStandardMaterial />
    </mesh>
  );
}
```

## Good Example 1 - Change scale, keep the geometry

```jsx
// GOOD - Unit geometry built once, size applied as scale
function GrowingBox() {
  const [size, setSize] = useState(1);
  return (
    <mesh scale={size} onClick={() => setSize((s) => s + 0.1)}>
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  );
}
```

For continuous changes, set `ref.current.scale` in `useFrame` instead of going through state.

## Bad Example 2 - New object inside args

```jsx
// BAD - A new object literal / instance on every render → rebuilt on every render
<meshStandardMaterial args={[{ color, roughness: 0.5 }]} />
<arrowHelper args={[new THREE.Vector3(0, 1, 0), new THREE.Vector3(), 1]} />
```

## Good Example 2 - Props for settable values, stable objects for args

```jsx
// GOOD - Material options are plain properties: set them as props
<meshStandardMaterial color={color} roughness={0.5} />

// GOOD - Objects that must go through args are created once
const dir = useMemo(() => new THREE.Vector3(0, 1, 0), []);
const origin = useMemo(() => new THREE.Vector3(), []);
<arrowHelper args={[dir, origin, 1]} />
```

## What does not rebuild

- An inline array of the same primitive values: `args={[1, 2, 3]}` creates a new array, but every element is `===` the previous one, so nothing happens.
- Changing ordinary props (`position`, `color`, `visible`, ...): R3F applies them to the existing object.

Use `args` only for values that really require a new object (e.g. geometry segment counts), and expect a rebuild when they change.
