# postpro-custom-shader

---

title: Create custom effects with shaders.
impact: MEDIUM

---

```jsx
import { Effect } from "postprocessing";
import { forwardRef, useMemo } from "react";
import { Uniform } from "three";

const fragmentShader = `
  uniform float intensity;

  void mainImage(const in vec4 inputColor, const in vec2 uv, out vec4 outputColor) {
    outputColor = vec4(inputColor.rgb * intensity, inputColor.a);
  }
`;

class CustomEffectImpl extends Effect {
  constructor({ intensity = 1.0 }) {
    super("CustomEffect", fragmentShader, {
      uniforms: new Map([["intensity", new Uniform(intensity)]]),
    });
  }
}

const CustomEffect = forwardRef(({ intensity }, ref) => {
  const effect = useMemo(
    () => new CustomEffectImpl({ intensity }),
    [intensity],
  );
  return <primitive ref={ref} object={effect} />;
});

// Usage
<EffectComposer>
  <CustomEffect intensity={0.5} />
</EffectComposer>;
```
