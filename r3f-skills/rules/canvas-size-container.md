# canvas-size-container

---

title: Canvas should fill its parent container.
impact: HIGH

---

## Canvas fills parent

```jsx
// CSS - Parent must have dimensions
.canvas-container {
  width: 100%;
  height: 100vh;
  /* or specific dimensions */
  width: 800px;
  height: 600px;
}

// JSX
<div className="canvas-container">
  <Canvas>
    <Scene />
  </Canvas>
</div>
```
