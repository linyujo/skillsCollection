# loading-use-progress

---

title: Use useProgress for loading progress UI.
impact: MEDIUM-HIGH

---

```jsx
import { useProgress, Html } from "@react-three/drei";

// loading progress UI
function Loader() {
  const { active, progress, errors, item, loaded, total } = useProgress();

  return (
    <Html center>
      <div className="loader">
        {progress.toFixed(0)}% loaded
        <br />
        Loading: {item}
      </div>
    </Html>
  );
}

function App() {
  return (
    <Canvas>
      <Suspense fallback={<Loader />}>
        <Scene />
      </Suspense>
    </Canvas>
  );
}
```
