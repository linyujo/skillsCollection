# loading-lazy-components

---

title: Lazy load heavy scene components.
impact: MEDIUM-HIGH

---

```jsx
import { lazy, Suspense } from "react";

const HeavyScene = lazy(() => import("./HeavyScene"));

function App() {
  const [showHeavy, setShowHeavy] = useState(false);

  return (
    <Canvas>
      <BasicScene />
      {showHeavy && (
        <Suspense fallback={null}>
          <HeavyScene />
        </Suspense>
      )}
    </Canvas>
  );
}
```
