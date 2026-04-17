# postpro-common-effects

---

title: Common post-processing effects.
impact: MEDIUM

---

```jsx
import {
  EffectComposer,
  Bloom,
  ChromaticAberration,
  DepthOfField,
  Noise,
  Vignette,
  SMAA,
  ToneMapping,
  HueSaturation,
  BrightnessContrast,
  SSAO,
  Outline,
  SelectiveBloom,
} from "@react-three/postprocessing";
```

## Bloom for glow

```jsx
<Bloom intensity={1} luminanceThreshold={0.5} luminanceSmoothing={0.9} />
```

## Depth of Field

```jsx
<DepthOfField focusDistance={0} focalLength={0.02} bokehScale={2} />
```

## Anti-aliasing

```jsx
<SMAA />
```

## Screen-space ambient occlusion

```jsx
<SSAO samples={31} radius={0.1} intensity={20} />
```

## Outline selected objects

```jsx
<Outline selection={selectedRef} edgeStrength={3} />
```
