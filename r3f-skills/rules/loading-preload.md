# loading-preload

---

title: Preload assets outside render cycle.
impact: MEDIUM-HIGH

---

```jsx
import { useGLTF, useTexture } from "@react-three/drei";

// Preload at module level
useGLTF.preload("/model.glb");
useTexture.preload("/texture.png");

// Or preload multiple
useGLTF.preload(["/model1.glb", "/model2.glb"]);
```
