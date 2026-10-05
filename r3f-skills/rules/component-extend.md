---
name: component-extend
title: "Use the v9 extend() API and ThreeElements typing."
impact: HIGH
---

# component-extend

`extend()` registers Three.js classes that are not in R3F's built-in catalogue (addons, third-party or your own classes) so they can be used as JSX.

## Good Example 1 - extend() returns a component (v9)

```tsx
import { extend } from "@react-three/fiber";
import { MyCustomMesh } from "./MyCustomMesh";

// v9: passing a class returns a typed component, no global registration
const CustomMesh = extend(MyCustomMesh);

function Scene() {
  return <CustomMesh args={[1, 2]} />;
}
```

## Good Example 2 - Object form + ThreeElements typing

```tsx
import { extend, type ThreeElement } from "@react-three/fiber";
import { MyCustomMesh } from "./MyCustomMesh";

// Register once at module level
extend({ MyCustomMesh });

// Augment R3F's element map, not the global JSX namespace
declare module "@react-three/fiber" {
  interface ThreeElements {
    myCustomMesh: ThreeElement<typeof MyCustomMesh>;
  }
}

function Scene() {
  return <myCustomMesh args={[1, 2]} />;
}
```

## Bad Example - Pre-v9 / pre-React 19 typing

```tsx
// BAD - React 19 removed the global JSX namespace
declare global {
  namespace JSX {
    interface IntrinsicElements {
      myCustomMesh: Object3DNode<MyCustomMesh, typeof MyCustomMesh>;
    }
  }
}

// BAD - Object3DNode / MaterialNode / BufferGeometryNode are v8 types
```

## Notes

- Call `extend({ ... })` at module level, not inside a component.
