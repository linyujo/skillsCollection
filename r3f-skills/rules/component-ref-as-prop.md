---
name: component-ref-as-prop
title: "In React 19, pass ref as a regular prop instead of forwardRef."
impact: HIGH
impactDescription: "React 19 passes ref to function components as a normal prop. forwardRef is no longer needed and is planned for deprecation; most existing R3F examples still use it."
---

# component-ref-as-prop

## Bad Example

```jsx
// BAD - Pre-React 19 pattern
import { forwardRef } from "react";

const Box = forwardRef(function Box({ color = "orange", ...props }, ref) {
  return (
    <mesh ref={ref} {...props}>
      <boxGeometry />
      <meshStandardMaterial color={color} />
    </mesh>
  );
});
```

## Good Example

```jsx
// GOOD - ref is just a prop
function Box({ ref, color = "orange", ...props }) {
  return (
    <mesh ref={ref} {...props}>
      <boxGeometry />
      <meshStandardMaterial color={color} />
    </mesh>
  );
}

function Scene() {
  const boxRef = useRef();

  useFrame((_, delta) => {
    boxRef.current.rotation.x += delta;
  });

  return <Box ref={boxRef} position={[0, 1, 0]} color="blue" />;
}
```

## TypeScript

```tsx
import type { ThreeElements } from "@react-three/fiber";

// ThreeElements["mesh"] already includes `ref?: Ref<THREE.Mesh>`
type BoxProps = ThreeElements["mesh"] & {
  color?: string;
};

function Box({ ref, color = "orange", ...props }: BoxProps) {
  return (
    <mesh ref={ref} {...props}>
      <boxGeometry />
      <meshStandardMaterial color={color} />
    </mesh>
  );
}
```

## Notes

- `useImperativeHandle(ref, () => api)` works the same way with the `ref` prop.
- Ref callbacks can return a cleanup function in React 19: `ref={(mesh) => { register(mesh); return () => unregister(mesh); }}`.
- Class components still receive `ref` as the instance, not as a prop.
