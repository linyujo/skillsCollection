# frame-conditional-subscription

---

title: Disable useFrame when not needed.
impact: CRITICAL

---

## Version Compatibility

How `useFrame(callback, renderPriority)` treats `renderPriority` differs between R3F major versions:

| R3F version | `renderPriority` semantics                                                                        | "Disable subscription" technique                            |
| ----------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **v9+**     | Accepts `null` to skip subscription (or a number for sort order)                                  | Pass `null` as priority → callback is not subscribed at all |
| **v8.x**    | Number only (default `0`); purely a sort key. Subscription is **unconditional** if hook is called | Use **early-return inside the callback** (Example 3)        |

If you target both versions or are unsure, the early-return pattern (Example 2) works everywhere.

## Bad Example

```jsx
// BAD - Always running

function BadAnimation() {
  useFrame((state, delta) => {
    ref.current.rotation.y += delta * 2;
  });
}
```

## Good Example 1 — v9+ (priority `null` disables subscription)

```jsx
// GOOD - Active only when needed (R3F v9+)

function GoodAnimation({ active }) {
  useFrame(
    () => {
      // Animation logic
    },
    active ? 0 : null,
  ); // null disables the subscription
}
```

When `active` flips to `false`, R3F unsubscribes the callback entirely — it is not invoked at all by the render loop.

## Good Example 2 — Universal (early return, works in v8.x and v9+)

```jsx
// GOOD - Alternative with early return

function ConditionalAnimation({ paused }) {
  useFrame((state, delta) => {
    if (paused) return;
    // Animation logic
  });
}
```

## Good Example 3 — v8.x (early return is the only available pattern)

In R3F v8.x, `useFrame` always subscribes when it is called; `renderPriority` is only used to sort callbacks among each other. The relevant runtime code (from `@react-three/fiber@8.18`):

```js
// node_modules/@react-three/fiber — useFrame implementation
function useFrame(callback, renderPriority = 0) {
  const subscribe = store.getState().internal.subscribe;
  const ref = useMutableCallback(callback);
  // Always subscribes when callback is provided; renderPriority is only a sort key
  useIsomorphicLayoutEffect(
    () => subscribe(ref, renderPriority, store),
    [renderPriority, subscribe, store],
  );
}
```

Passing `null` at runtime does **not** opt out of subscription in v8.x (and the TypeScript types reject it: `renderPriority?: number`). The canonical pattern is therefore ref-based gating + early return inside the callback:

```jsx
// v8.x: ref-based gate + early return inside callback (one-shot animation)

function OneShotAnimation() {
  const playingRef = useRef(false);
  const elapsedRef = useRef(0);

  const start = () => {
    elapsedRef.current = 0;
    playingRef.current = true;
  };

  useFrame((_, delta) => {
    if (!playingRef.current) return; // ~1 ns when idle
    elapsedRef.current += delta;
    // Animation logic — mutate refs / Three.js objects directly (no setState)
    if (elapsedRef.current >= TOTAL_DURATION) {
      playingRef.current = false; // mark done; subsequent frames early-return
    }
  });

  // ...
}
```

Idle cost: a ref dereference + a boolean negation + a conditional jump per frame — single-digit nanoseconds at 60 fps. For one-shot or rarely-active animations, this overhead is negligible compared to upgrading R3F just for this optimization.

### Why not use React state for the gate in v8.x?

You might be tempted to mirror `playing` into `useState` so a re-render can toggle the priority:

```jsx
// Tempting but broken in v8.x
const [playing, setPlaying] = useState(false);
useFrame(callback, playing ? 0 : null); // TS error; null still subscribes at runtime
```

Two problems:

1. **TypeScript** — v8.x types `renderPriority` as `number | undefined`; `null` is rejected.
2. **Runtime** — even if you cast and pass `null`, the implementation above still calls `subscribe(ref, null, store)`. The callback runs; you have not avoided anything.

Stick with refs + early return until you migrate to v9.
