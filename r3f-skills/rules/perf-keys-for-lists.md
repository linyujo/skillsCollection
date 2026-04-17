# perf-keys-for-lists

---

title: Use stable keys for dynamic lists.
impact: CRITICAL

---

## Bad Example

```jsx
// BAD - Index as key causes unnecessary remounts

function Particles({ particles }) {
  return particles.map((p, i) => (
    <Particle key={i} position={p.position} /> // Index changes when array changes
  ));
}
```

## Good Example

```jsx
// GOOD - Stable unique ID

function Particles({ particles }) {
  return particles.map((p) => (
    <Particle key={p.id} position={p.position} /> // Stable ID
  ));
}
```
