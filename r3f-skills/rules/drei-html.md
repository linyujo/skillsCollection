# drei-html

---

title: Use Html for DOM overlays in 3D space.
impact: MEDIUM-HIGH

---

```jsx
import { Html } from "@react-three/drei";

function Label({ position, text }) {
  return (
    <Html
      position={position}
      center // Center the HTML element
      distanceFactor={10} // Scale with distance
      occlude // Hide when behind objects
      transform // Use CSS3D transforms
    >
      <div className="label">{text}</div>
    </Html>
  );
}
```
