---
name: r3f-best-practices
description: React Three Fiber (R3F) and Poimandres ecosystem decision framework. Use when writing, reviewing, or optimizing R3F code.
metadata:
  author: three-agent-skills
  version: "1.1.0"
---

## When to Apply

Reference these guidelines when:

- Writing new R3F components
- Optimizing R3F performance (re-renders are the #1 issue)
- Managing state with Zustand

## Ecosystem Coverage

- **@react-three/fiber** - React renderer for Three.js
- **zustand** - State management

## Rule Categories by Priority

| Priority | Category                 | Impact      | Rule Prefix  |
| -------- | ------------------------ | ----------- | ------------ |
| 1        | Performance & Re-renders | CRITICAL    | `perf-`      |
| 2        | useFrame & Animation     | CRITICAL    | `frame-`     |
| 3        | Component Patterns       | HIGH        | `component-` |
| 4        | Canvas & Setup           | HIGH        | `canvas-`    |
| 7        | State Management         | MEDIUM      | `state-`     |
| 8        | Events & Interaction     | MEDIUM      | `events-`    |

## Quick Route

| Scenario           | Key Features / Keywords                             | Category                                                           |
| ------------------ | --------------------------------------------------- | ------------------------------------------------------------------ |
| Scene setup        | Canvas, Context, Lights, Shadows, Basic config      | Canvas & Setup, Component Patterns                                 |
| Simple viewer      | useGLTF, .glb/.gltf, Preloading, Environment        | Performance & Re-renders                                           |
| HTML / UI Overlays | Html, Text, DOM elements in 3D, Annotations, UI     | Events & Interaction, Performance & Re-renders                     |
| Custom geometry    | bufferGeometry, 3D shapes, Attributes, Vertices     | Component Patterns, Performance & Re-renders                       |
| Particles / VFX    | Points, InstancedMesh, Math heavy, Frame delta      | useFrame & Animation, Performance & Re-renders                     |
| Shader art         | shaderMaterial, Uniforms, GLSL, Procedural          | useFrame & Animation, Performance & Re-renders, Component Patterns |
| Interactivity      | onClick, onPointerOver, Raycasting, Hover states    | Events & Interaction, Component Patterns                           |
| Global State       | Zustand, Cross-component state, UI-to-3D comms      | State Management, Performance & Re-renders                         |
| Camera Controls    | OrbitControls, PresentationControls, Lerp           | useFrame & Animation, Events & Interaction                         |
| Game/simulation    | Complex logic, Multiple systems, Optimization heavy | All skills                                                         |

## How to Use Categories

Read individual rule files for detailed explanations and code examples:

1. Go to Quick Reference
2. Find the category that matches your needs
3. Read the rules in that category
4. Apply the rules to your code

```
rules/perf-never-set-state-in-useframe.md
rules/perf-zustand-selectors.md
```

## Quick Reference

### 1. Performance & Re-renders (CRITICAL)

React re-renders are the #1 performance killer in R3F. The render loop runs at 60fps - React reconciliation must not interfere.

- `perf-never-set-state-in-useframe` - NEVER call setState in useFrame
- `perf-isolate-state` - Isolate components that need React state
- `perf-zustand-selectors` - Zustand v5 selectors, useShallow, transient reads, subscribeWithSelector
- `perf-dispose-auto` - What R3F disposes, dispose={null}, and resources you must dispose yourself
- `perf-visibility-toggle` - Toggle visibility instead of remounting

### 2. useFrame & Animation (CRITICAL)

useFrame is R3F's render loop hook. Misuse causes performance disasters.

- `frame-priority` - Positive priority takes over rendering; order with negative numbers and 0
- `frame-delta-time` - Always use delta for animations
- `frame-conditional-subscription` - Unmount to unsubscribe, early return to pause
- `frame-render-on-demand` - Use invalidate() for on-demand rendering
- `frame-no-allocation` - Don't allocate objects inside useFrame

### 3. Component Patterns (HIGH)

- `component-primitive` - Clone loaded models correctly before reusing them
- `component-extend` - Use the v9 extend() API and ThreeElements typing
- `component-ref-as-prop` - React 19: pass ref as a prop instead of forwardRef
- `component-args-reconstruct` - Changing args rebuilds the whole object

### 4. Canvas & Setup (HIGH)

Proper Canvas configuration

- `canvas-linear-flat` - Don't override R3F's color management
- `canvas-shadows` - Use shadows="percentage"; PCFSoftShadowMap was removed

### 7. State Management (MEDIUM)

Zustand is the recommended state manager for R3F.

- `state-avoid-objects-in-store` - Be careful with Three.js objects

### 8. Events & Interaction (MEDIUM)

- `events-stop-propagation` - Events pass through objects; stop them explicitly

## Quick Reference Card

### Critical (Always Do)

- [ ] NEVER use setState in useFrame
- [ ] Use Zustand selectors (not entire store); wrap object/array selectors in useShallow
- [ ] Use refs for animation, not state
- [ ] Use delta time for animations
- [ ] Never use a positive useFrame priority just for ordering
- [ ] No allocation in useFrame (no new / clone; reuse scratch objects)

### High Priority

- [ ] Don't change args to animate; use props like scale instead
- [ ] Pass ref as a prop (React 19), no forwardRef
- [ ] Dispose resources you create with new / useMemo; use dispose={null} only for JSX resources shared via ref
- [ ] Clone cached models with SkeletonUtils.clone inside useMemo
- [ ] Don't override R3F's default color management
- [ ] Use shadows="percentage", not shadows / shadows="soft"

### Poimandres Ecosystem

- [ ] Zustand: Selectors, transient subscriptions (subscribe(selector, listener) needs subscribeWithSelector)

## Sources & Credits

> Additional tips from [100 Three.js Tips](https://www.utsubo.com/blog/threejs-best-practices-100-tips) by [Utsubo](https://www.utsubo.com)
> Original document: [three-agent-skills](https://github.com/emalorenzo/three-agent-skills) by [Emanuel Lorenzo](https://github.com/emalorenzo)
> R3F Router: [r3f-router](https://github.com/Bbeierle12/Skill-MCP-Claude/blob/main/skills/r3f-router/SKILL.md) by [Bbeierle12](https://github.com/Bbeierle12)
