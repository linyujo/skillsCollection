# state-persist

---

title: Persist state across sessions when needed.
impact: MEDIUM

---

```jsx
import { persist } from "zustand/middleware";

const useSettingsStore = create(
  persist(
    (set) => ({
      musicVolume: 0.8,
      sfxVolume: 1.0,
      setMusicVolume: (vol) => set({ musicVolume: vol }),
    }),
    {
      name: "game-settings",
    },
  ),
);
```
