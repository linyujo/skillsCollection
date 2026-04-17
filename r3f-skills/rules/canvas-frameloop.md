# canvas-frameloop

---

title: Choose appropriate frameloop mode.
impact: HIGH

---

## Default frameloop

```jsx
<Canvas frameloop="always">{/* Scene */}</Canvas>
```

## Render on demand - call invalidate() to render

```jsx
<Canvas frameloop="demand">{/* Scene */}</Canvas>
```

## Never auto-render - call advance() manually

```jsx
<Canvas frameloop="never">{/* Scene */}</Canvas>
```
