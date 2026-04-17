# drei-use-texture

---

title: Use useTexture for texture loading.
impact: MEDIUM-HIGH

---

```jsx
import { useTexture } from "@react-three/drei";

function TexturedMesh() {
  // Single texture
  const texture = useTexture("/texture.png");

  // Multiple textures
  const [colorMap, normalMap, roughnessMap] = useTexture([
    "/color.png",
    "/normal.png",
    "/roughness.png",
  ]);

  // Object form
  const textures = useTexture({
    map: "/color.png",
    normalMap: "/normal.png",
    roughnessMap: "/roughness.png",
  });

  return (
    <mesh>
      <boxGeometry />
      <meshStandardMaterial {...textures} />
    </mesh>
  );
}

// Preload
useTexture.preload("/texture.png");
```
