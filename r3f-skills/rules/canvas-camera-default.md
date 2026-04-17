# canvas-camera-default

---

title: Configure default camera via camera prop.
impact: HIGH

---

## Perspective camera (default)

```jsx
<Canvas camera={{ position: [0, 5, 10], fov: 75, near: 0.1, far: 1000 }}>
  {/* Scene */}
</Canvas>
```

## Orthographic camera

```jsx
<Canvas camera={{ position: [0, 5, 10], zoom: 100 }}>{/* Scene */}</Canvas>
```

## Make camera manual (don't respond to resize)

```jsx
<Canvas camera={{ manual: true }}>{/* Scene */}</Canvas>
```
