# state-subscribeWithSelector

---

title: Use subscribeWithSelector for fine-grained subscriptions.
impact: MEDIUM

---

```jsx
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

const useStore = create(
  subscribeWithSelector((set) => ({
    score: 0,
    combo: 0,
    // ...
  })),
);

// Subscribe to specific changes
useEffect(() => {
  const unsub = useStore.subscribe(
    (state) => state.score,
    (score, prevScore) => {
      console.log("Score changed from", prevScore, "to", score);
      playScoreSound();
    },
  );
  return unsub;
}, []);
```
