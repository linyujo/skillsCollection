# leva-conditional

---

title: Hide Leva in production.
impact: LOW

---

```jsx
import { Leva } from "leva";

function App() {
  return (
    <>
      <Leva hidden={process.env.NODE_ENV === "production"} />
      <Canvas>
        <Scene />
      </Canvas>
    </>
  );
}
```
