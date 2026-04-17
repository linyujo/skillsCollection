# state-separate-concerns

---

title: Separate stores by concern.
impact: MEDIUM

---

```jsx
// Game state
const useGameStore = create((set) => ({
  score: 0,
  level: 1,
  // ...
}));

// Player state
const usePlayerStore = create((set) => ({
  health: 100,
  inventory: [],
  // ...
}));

// UI state
const useUIStore = create((set) => ({
  isPaused: false,
  showInventory: false,
  // ...
}));
```
