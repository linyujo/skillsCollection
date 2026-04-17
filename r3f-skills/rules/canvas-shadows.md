# canvas-shadows

---

title: Enable shadows at Canvas level.
impact: HIGH

---

## Enable Basic shadows

```jsx
<Canvas shadows>{/* Scene */}</Canvas>
```

## Enable Soft shadows (PCFSoft)

```jsx
<Canvas shadows="soft">{/* Scene */}</Canvas>
```

## On lights and meshes

```jsx
<directionalLight castShadow shadow-mapSize={[2048, 2048]} />
<mesh castShadow receiveShadow>
```
