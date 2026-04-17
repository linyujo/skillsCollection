# component-extend

---

title: Use extend() for custom Three.js classes.
impact: HIGH

---

## For custom Three.js classes

```jsx
import { extend } from "@react-three/fiber";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";

// Register once at module level
extend({ OrbitControls, EffectComposer });

// Now use as JSX
function Scene() {
  const { camera, gl } = useThree();
  return (
    <>
      <orbitControls args={[camera, gl.domElement]} />
    </>
  );
}
```
