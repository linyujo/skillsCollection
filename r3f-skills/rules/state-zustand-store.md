# state-zustand-store

---

title: Create focused stores for game/app state.
impact: MEDIUM

---

```jsx
import { create } from "zustand";

const useGameStore = create((set, get) => ({
  // State
  score: 0,
  health: 100,
  position: new THREE.Vector3(),

  // Actions
  increaseScore: (amount) => set((state) => ({ score: state.score + amount })),
  damage: (amount) =>
    set((state) => ({ health: Math.max(0, state.health - amount) })),
  setPosition: (pos) => set({ position: pos }),

  // Computed (use get() for derived state in actions)
  reset: () => set({ score: 0, health: 100, position: new THREE.Vector3() }),
}));
```
