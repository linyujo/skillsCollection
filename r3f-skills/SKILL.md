---
name: r3f-best-practices
description: Version traps and counter-intuitive pitfalls for React Three Fiber (@react-three/fiber v9) with React 19, three r183+ and Zustand v5. Use when writing or reviewing R3F code that involves useFrame, <Canvas> props (shadows, linear, flat, frameloop), useGLTF / primitive cloning, dispose, args, extend, refs, pointer events, or Zustand stores.
metadata:
  author: Raine
  version: "2.0.0"
  verified-against: "react 19.3, @react-three/fiber 9.8, three 0.186, zustand 5.0.15 (2026-10)"
---

# R3F pitfalls

Assumes React 19, @react-three/fiber 9, three r183+ and Zustand 5. Check `package.json` first: on older versions, the rows marked **(v)** may not apply (the recommended API may not exist yet, or the old behavior may still be correct). Read the rule file before applying them.

Each row is a pattern to look for in code. When writing code, avoid the left column; when reviewing, scan for it. Open `rules/<rule>.md` for the full explanation and examples.

## useFrame

| If the code has… | Problem | Do instead | Rule |
| --- | --- | --- | --- |
| `setState` inside `useFrame` | 60+ React re-renders per second | Mutate `ref.current` directly | `perf-never-set-state-in-useframe` |
| `new THREE.*()`, `.clone()`, new arrays / objects inside `useFrame` | GC pauses, frame drops | Reuse scratch objects (module scope or `useMemo`) with `.set()` / `.copy()` | `frame-no-allocation` |
| `+= 0.01` or `lerp(target, 0.1)` per frame | Speed depends on frame rate | Multiply by `delta`; lerp factor `1 - Math.pow(k, delta)` or `MathUtils.damp` | `frame-delta-time` |
| `useFrame(fn, n)` with `n > 0` | R3F stops auto-rendering; screen freezes unless `fn` renders | Order with negative numbers and `0`; use `> 0` only when `fn` renders (composer, HUD, viewports) | `frame-priority` |
| `useFrame(fn, cond ? 0 : null)` to pause | Still subscribed, runs every frame | Unmount the component, or return early in `fn` | `frame-priority` |
| `frameloop="demand"` + scene changed outside React (store subscription, DOM event, tween) | Change never reaches the screen | Call `invalidate()`, taken via `useThree((s) => s.invalidate)` | `frame-render-on-demand` |

## Resources and components

| If the code has… | Problem | Do instead | Rule |
| --- | --- | --- | --- |
| `{show && <Heavy />}` toggled often | Rebuild, GPU upload and shader recompile on every toggle | `visible={show}` | `perf-visibility-toggle` |
| `new THREE.*Geometry / *Material / Texture / WebGLRenderTarget` in `useMemo` without cleanup | GPU memory leak (R3F never disposes these) | `.dispose()` in a `useEffect` cleanup | `perf-dispose-auto` |
| JSX material / geometry shared with other meshes through a ref | Disposed when its owner unmounts | `dispose={null}` on it, or create it in the common parent | `perf-dispose-auto` |
| One `useGLTF` scene in several `<primitive>`s; `scene.clone()` in render | Only one copy visible; clones on every render; skinned meshes break | `useMemo(() => SkeletonUtils.clone(scene), [scene])` or drei `<Clone>` | `component-primitive` |
| `args` driven by state / props, or new objects inside `args` | Object is disposed and rebuilt on every change | Settable props (`scale`, `color`, …); `useMemo` for object args | `component-args-reconstruct` |
| **(v)** `forwardRef` | Unnecessary since React 19 | `function C({ ref, ...props })` | `component-ref-as-prop` |
| **(v)** `declare global { namespace JSX … }`, `Object3DNode` | Pre-v9 / pre-React 19 typing | Augment `ThreeElements`, or `const X = extend(Class)` | `component-extend` |

## Canvas and events

| If the code has… | Problem | Do instead | Rule |
| --- | --- | --- | --- |
| **(v)** `outputEncoding`, `sRGBEncoding`, `texture.encoding`; `linear` / `flat` added by habit | Removed API; wrong colors | Keep R3F's defaults; use `colorSpace` | `canvas-linear-flat` |
| **(v)** `<Canvas shadows>`, `shadows="soft"`, `PCFSoftShadowMap` | No longer supported by three: warning + fallback | `shadows="percentage"` + light `shadow-radius` | `canvas-shadows` |
| Overlapping meshes with `onClick` / `onPointerOver` | Objects behind also receive the event | `e.stopPropagation()` in the front handler | `events-stop-propagation` |

## Zustand

| If the code has… | Problem | Do instead | Rule |
| --- | --- | --- | --- |
| **(v)** `useStore()`, `useStore(sel, shallow)`, or a selector returning a new object / array | Re-render on every change; infinite render loop in v5 | One value per selector, or `useShallow`; `getState()` inside `useFrame` | `perf-zustand-selectors` |
| **(v)** `store.subscribe(selector, listener)` on a plain store | Listener is never called | Create the store with `subscribeWithSelector` | `perf-zustand-selectors` |

## Maintenance

Rules marked **(v)** depend on library versions. When upgrading any package listed in `verified-against`, re-check those rules against the new source and update `verified-against`.

## Sources & Credits

> Additional tips from [100 Three.js Tips](https://www.utsubo.com/blog/threejs-best-practices-100-tips) by [Utsubo](https://www.utsubo.com)
> Original document: [three-agent-skills](https://github.com/emalorenzo/three-agent-skills) by [Emanuel Lorenzo](https://github.com/emalorenzo)
> R3F Router: [r3f-router](https://github.com/Bbeierle12/Skill-MCP-Claude/blob/main/skills/r3f-router/SKILL.md) by [Bbeierle12](https://github.com/Bbeierle12)
