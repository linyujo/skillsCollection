# state-avoid-objects-in-store

---

title: Avoid storing Three.js objects directly in Zustand.
impact: MEDIUM
impactDescription: Three.js objects are mutable and don't trigger re-renders on internal changes.

---

## Bad Example

```jsx
// PROBLEMATIC - Mutating Vector3 won't trigger re-renders
const useStore = create((set) => ({
  position: new THREE.Vector3(), // Object reference stays same
  updatePosition: (x, y, z) => {
    const pos = get().position;
    pos.set(x, y, z); // Mutation, no re-render!
    set({ position: pos }); // Same reference, might not trigger
  },
}));
```

## Good Example

```jsx
// BETTER - Store primitives
const useStore = create((set) => ({
  positionX: 0,
  positionY: 0,
  positionZ: 0,
  setPosition: (x, y, z) => set({ positionX: x, positionY: y, positionZ: z }),
}));
```

## Good Example 2

```jsx
// OR - Create new object reference
const useStore = create((set) => ({
  position: new THREE.Vector3(),
  setPosition: (x, y, z) => set({ position: new THREE.Vector3(x, y, z) }),
}));
```
