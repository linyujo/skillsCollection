---
name: canvas-shadows
title: "Use shadows=\"percentage\"; PCFSoftShadowMap was removed from three."
impact: HIGH
impactDescription: "Current three (verified on r186) no longer supports PCFSoftShadowMap. R3F v9's default shadows setting still selects it, so three logs a warning and falls back to PCFShadowMap."
---

# canvas-shadows

## What happens

| `<Canvas shadows=…>` | R3F v9 sets           | three r186                                      |
| -------------------- | --------------------- | ----------------------------------------------- |
| `true` (`shadows`)   | `PCFSoftShadowMap`    | Warns "PCFSoftShadowMap has been removed", uses `PCFShadowMap` |
| `"soft"`             | `PCFSoftShadowMap`    | Same warning and fallback                        |
| `"percentage"`       | `PCFShadowMap`        | No warning                                       |
| `"basic"`            | `BasicShadowMap`      | Hard, aliased edges                              |
| `"variance"`         | `VSMShadowMap`        | Soft, can show light bleeding                    |

The current `PCFShadowMap` is already soft (Vogel-disk sampling). Its softness is controlled per light with `shadow.radius`.

## Bad Example

```jsx
// BAD - All three select the removed PCFSoftShadowMap
<Canvas shadows>
<Canvas shadows="soft">
<Canvas onCreated={({ gl }) => { gl.shadowMap.type = THREE.PCFSoftShadowMap; }}>
```

## Good Example

```jsx
// GOOD - Same visual result, no warning
<Canvas shadows="percentage">
  <directionalLight
    castShadow
    position={[5, 10, 5]}
    shadow-mapSize={[2048, 2048]}
    shadow-radius={4} // Softness of PCF shadows (default 1)
  />
  <mesh castShadow receiveShadow>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</Canvas>
```

## Notes

- Shadows need all three: `shadows` on `<Canvas>`, `castShadow` on the light, and `castShadow` / `receiveShadow` on meshes.
- The object form `shadows={{ type: THREE.PCFShadowMap }}` also works and is assigned directly to `gl.shadowMap`.
