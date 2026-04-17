# perf-r3f-perf

---

title: Use r3f-perf for performance monitoring.
impact: CRITICAL

---

Use r3f-perf for comprehensive React Three Fiber performance monitoring.

## Best Practices

- Remove in production - Always hide in production builds
- Use sparingly - Performance monitor itself has overhead
- Check draw calls - Target under 100 draw calls
- Monitor memory - Watch for leaking geometries/textures
- Use alongside renderer.info - For detailed WebGL stats

## Conditional Rendering for Production

```jsx
// PROD - Never show in production
import { Perf } from "r3f-perf";

function App() {
  const isDev = process.env.NODE_ENV === "development";

  return (
    <Canvas>
      {isDev && <Perf position="top-left" />}
      <Scene />
    </Canvas>
  );
}
```

## Deep Analyze Mode

For detailed per-object analysis:
Shows render times for individual objects but has higher CPU overhead.

```jsx
// Deep analyze mode - shows per-object stats

<Perf deepAnalyze={true} className="custom-perf" />
```
