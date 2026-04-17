# postpro-performance

---

title: Optimize post-processing performance.
impact: MEDIUM

---

```jsx
<EffectComposer
  multisampling={0} // Disable MSAA (use SMAA instead)
  frameBufferType={THREE.HalfFloatType} // Use half-float for better performance
>
  <SMAA /> {/* Cheaper than MSAA */}
  <Bloom mipmapBlur /> {/* mipmapBlur is more efficient */}
</EffectComposer>
```
