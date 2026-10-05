# perf-zustand-selectors

---

title: Use Zustand v5 selectors to minimize re-renders.
impact: CRITICAL
impactDescription: Subscribing to the entire store re-renders on every change. In Zustand v5, a selector that returns a new object or array on every call causes an infinite render loop.

---

Zustand v5 changed the hook signature: `useStore(selector)` takes **one** argument. The v4 equality-function argument (`useStore(selector, shallow)`) no longer exists and is silently ignored.

## Bad Example 1 - Whole store

```jsx
// BAD - Re-renders on ANY store change
function Player() {
  const store = useGameStore();
  return <mesh position-x={store.playerX} />;
}
```

## Bad Example 2 - v4 equality argument

```jsx
// BAD - v4 style. In v5 `shallow` is ignored; the selector returns a new
// object on every call → "Maximum update depth exceeded"
import { shallow } from "zustand/shallow";

const { x, y } = useGameStore((s) => ({ x: s.x, y: s.y }), shallow);
```

## Good Example 1 - One value per selector

```jsx
// GOOD - Re-renders only when playerX changes
const playerX = useGameStore((s) => s.playerX);
```

## Good Example 2 - Several values with useShallow

```jsx
// GOOD - useShallow keeps the result stable while x and y are unchanged
import { useShallow } from "zustand/react/shallow";

const { x, y } = useGameStore(useShallow((s) => ({ x: s.x, y: s.y })));
const [health, score] = useGameStore(useShallow((s) => [s.health, s.score]));
```

To keep the v4 two-argument form in an existing codebase, create the store with `createWithEqualityFn` from `zustand/traditional` (requires the `use-sync-external-store` package). Prefer `useShallow` for new code.

## Reading without re-rendering

For values that change every frame, don't subscribe through the hook at all.

### Inside useFrame: getState()

```jsx
function Follower() {
  const ref = useRef();

  useFrame((_, delta) => {
    const { target } = useGameStore.getState(); // No subscription, no re-render
    ref.current.position.lerp(target, 1 - Math.pow(0.001, delta));
  });

  return <mesh ref={ref} />;
}
```

### Outside useFrame: subscribe(listener)

A plain store's `subscribe` takes **only a listener** that receives the whole state:

```jsx
useEffect(
  () =>
    useGameStore.subscribe((state, prevState) => {
      if (state.score !== prevState.score) playScoreSound();
    }),
  [],
);
```

### subscribe(selector, listener) needs subscribeWithSelector

`subscribe(selector, listener, options)` only exists when the store is created with the `subscribeWithSelector` middleware. Without it, the selector is treated as the listener and the second function is never called.

```jsx
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";
import { shallow } from "zustand/shallow";

const useGameStore = create(
  subscribeWithSelector((set) => ({
    score: 0,
    playerPosition: [0, 0, 0],
    // ...
  })),
);

function PlayerMarker() {
  const ref = useRef();

  useEffect(
    () =>
      useGameStore.subscribe(
        (s) => s.playerPosition,
        (position) => ref.current.position.fromArray(position),
        {
          equalityFn: shallow, // Compare arrays/objects by content
          fireImmediately: true, // Run once with the current value
        },
      ),
    [],
  );

  return <mesh ref={ref} />;
}
```

## Comparison

| Method                                         | Re-renders                     | Use case                          |
| ---------------------------------------------- | ------------------------------ | --------------------------------- |
| `useStore()`                                   | Every change                   | Never                             |
| `useStore((s) => s.value)`                     | When `value` changes           | Most cases                        |
| `useStore(useShallow((s) => ({ a, b })))`      | When `a` or `b` changes        | Several values                    |
| `useStore.getState()`                          | Never                          | Inside useFrame / event handlers  |
| `useStore.subscribe(listener)`                 | Never                          | React to changes outside render   |
| `useStore.subscribe(selector, listener, opts)` | Never                          | Same, per slice (needs `subscribeWithSelector`) |

## References

- [Zustand v5 migration guide](https://github.com/pmndrs/zustand/blob/main/docs/migrations/migrating-to-v5.md)
