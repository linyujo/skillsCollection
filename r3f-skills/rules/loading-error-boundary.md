# loading-error-boundary

---

title: Handle loading errors with error boundaries.
impact: MEDIUM-HIGH

---

```jsx
import { ErrorBoundary } from "react-error-boundary";

function ModelErrorFallback({ error, resetErrorBoundary }) {
  return (
    <Html center>
      <div>
        <p>Failed to load model</p>
        <button onClick={resetErrorBoundary}>Try again</button>
      </div>
    </Html>
  );
}

function SafeModel({ url }) {
  return (
    <ErrorBoundary
      FallbackComponent={ModelErrorFallback}
      onReset={() => {
        // Reset any state if needed
      }}
    >
      <Suspense fallback={<LoadingBox />}>
        <Model url={url} />
      </Suspense>
    </ErrorBoundary>
  );
}
```
