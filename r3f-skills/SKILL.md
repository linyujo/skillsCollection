---
name: r3f-best-practices
description: React Three Fiber (R3F) and Poimandres ecosystem best practices. Use when writing, reviewing, or optimizing R3F code. Triggers on tasks involving @react-three/fiber, @react-three/drei, zustand, @react-three/postprocessing, @react-three/rapier, or leva.
metadata:
  author: three-agent-skills
  version: "1.1.0"
---

# React Three Fiber Best Practices

Comprehensive guide for React Three Fiber and the Poimandres ecosystem. Contains 70+ rules across 12 categories, prioritized by impact.

## Sources & Credits

> Additional tips from [100 Three.js Tips](https://www.utsubo.com/blog/threejs-best-practices-100-tips) by [Utsubo](https://www.utsubo.com)
> Original document: [three-agent-skills](https://github.com/emalorenzo/three-agent-skills) by [Emanuel Lorenzo](https://github.com/emalorenzo)

## When to Apply

Reference these guidelines when:

- Writing new R3F components
- Optimizing R3F performance (re-renders are the #1 issue)
- Using Drei helpers correctly
- Implementing post-processing or physics
- Managing state with Zustand

## Ecosystem Coverage

- **@react-three/fiber** - React renderer for Three.js
- **@react-three/drei** - Useful helpers and abstractions
- **@react-three/postprocessing** - Post-processing effects
- **@react-three/rapier** - Physics engine
- **zustand** - State management
- **leva** - Debug GUI

## Rule Categories by Priority

| Priority | Category                 | Impact      | Prefix       |
| -------- | ------------------------ | ----------- | ------------ |
| 1        | Performance & Re-renders | CRITICAL    | `perf-`      |
| 2        | useFrame & Animation     | CRITICAL    | `frame-`     |
| 3        | Component Patterns       | HIGH        | `component-` |
| 4        | Canvas & Setup           | HIGH        | `canvas-`    |
| 5        | Drei Helpers             | MEDIUM-HIGH | `drei-`      |
| 6        | Loading & Suspense       | MEDIUM-HIGH | `loading-`   |
| 7        | State Management         | MEDIUM      | `state-`     |
| 8        | Events & Interaction     | MEDIUM      | `events-`    |
| 9        | Post-processing          | MEDIUM      | `postpro-`   |
| 10       | Physics (Rapier)         | LOW-MEDIUM  | `physics-`   |
| 11       | Leva (Debug GUI)         | LOW         | `leva-`      |

## Quick Reference

### 1. Performance & Re-renders (CRITICAL)

React re-renders are the #1 performance killer in R3F. The render loop runs at 60fps - React reconciliation must not interfere.

- `perf-never-set-state-in-useframe` - NEVER call setState in useFrame
- `perf-isolate-state` - Isolate components that need React state
- `perf-zustand-selectors` - Use Zustand selectors, not entire store
- `perf-memo-components` - Memoize expensive components
- `perf-keys-for-lists` - Use stable keys for dynamic lists
- `perf-avoid-inline-objects` - Avoid creating objects/arrays in JSX
- `perf-dispose-auto` - Understand R3F auto-dispose behavior
- `perf-visibility-toggle` - Toggle visibility instead of remounting
- `perf-r3f-perf` - Use r3f-perf for performance monitoring

### 2. useFrame & Animation (CRITICAL)

useFrame is R3F's render loop hook. Misuse causes performance disasters.

- `frame-priority` - Use priority for execution order
- `frame-delta-time` - Always use delta for animations
- `frame-conditional-subscription` - Disable useFrame when not needed
- `frame-destructure-state` - Destructure only what you need
- `frame-render-on-demand` - Use invalidate() for on-demand rendering
- `frame-avoid-heavy-computation` - Move heavy work outside useFrame

### 3. Component Patterns (HIGH)

- `component-jsx-elements` - Use JSX for Three.js objects
- `component-attach-prop` - Use attach for non-standard properties
- `component-primitive` - Use primitive for existing objects
- `component-extend` - Use extend() for custom classes
- `component-forwardref` - Use forwardRef for reusable components
- `component-dispose-null` - Set dispose={null} on shared resources

### 4. Canvas & Setup (HIGH)

Proper Canvas configuration

- `canvas-size-container` - Canvas fills parent container
- `canvas-camera-default` - Configure camera via prop
- `canvas-gl-config` - Configure WebGL context
- `canvas-shadows` - Enable shadows at Canvas level
- `canvas-frameloop` - Choose appropriate frameloop mode
- `canvas-events` - Configure event handling
- `canvas-linear-flat` - Use linear/flat for correct colors

### 5. Drei Helpers (MEDIUM-HIGH)

Use @react-three/drei correctly

- `drei-use-gltf` - useGLTF with preloading
- `drei-use-texture` - useTexture for texture loading
- `drei-environment` - Environment for realistic lighting
- `drei-orbit-controls` - OrbitControls from Drei
- `drei-html` - Html for DOM overlays
- `drei-text` - Text for 3D text
- `drei-instances` - Instances for optimized instancing
- `drei-use-helper` - useHelper for debug visualization
- `drei-bounds` - Bounds to fit camera
- `drei-center` - Center to center objects
- `drei-float` - Float for floating animation

### 6. Loading & Suspense (MEDIUM-HIGH)

- `loading-suspense` - Wrap async components in Suspense
- `loading-preload` - Preload assets with useGLTF.preload
- `loading-use-progress` - useProgress for loading UI
- `loading-lazy-components` - Lazy load heavy components
- `loading-error-boundary` - Handle loading errors

### 7. State Management (MEDIUM)

Zustand is the recommended state manager for R3F.

- `state-zustand-store` - Create focused Zustand stores
- `state-avoid-objects-in-store` - Be careful with Three.js objects
- `state-subscribeWithSelector` - Fine-grained subscriptions
- `state-persist` - Persist state when needed
- `state-separate-concerns` - Separate stores by concern

### 8. Events & Interaction (MEDIUM)

- `events-pointer-events` - Use pointer events on meshes
- `events-stop-propagation` - Prevent event bubbling
- `events-cursor-pointer` - Change cursor on hover
- `events-raycast-filter` - Filter raycasting
- `events-event-data` - Understand event data structure

### 9. Post-processing (MEDIUM)

- `postpro-effect-composer` - Use EffectComposer
- `postpro-common-effects` - Common effects reference
- `postpro-selective-bloom` - SelectiveBloom for optimized glow
- `postpro-custom-shader` - Create custom effects
- `postpro-performance` - Optimize post-processing

### 10. Physics Rapier (LOW-MEDIUM)

- `physics-setup` - Basic Rapier setup
- `physics-body-types` - dynamic, fixed, kinematic
- `physics-colliders` - Choose appropriate colliders
- `physics-events` - Handle collision events
- `physics-api-ref` - Use ref for physics API
- `physics-performance` - Optimize physics

### 11. Leva (LOW)

- `leva-basic` - Basic Leva usage
- `leva-folders` - Organize with folders
- `leva-conditional` - Hide in production

## How to Use

Read individual rule files for detailed explanations and code examples:

```
rules/perf-never-set-state-in-useframe.md
rules/drei-use-gltf.md
rules/state-zustand-selectors.md
```

## Quick Reference Card

### Critical (Always Do)

- [ ] NEVER use setState in useFrame
- [ ] Use Zustand selectors (not entire store)
- [ ] Use refs for animation, not state
- [ ] Avoid inline objects/arrays in JSX
- [ ] Use delta time for animations
- [ ] Wrap async components in Suspense

### High Priority

- [ ] Memoize expensive components
- [ ] Use stable keys for dynamic lists
- [ ] Preload assets with useGLTF.preload
- [ ] Configure Canvas shadows properly
- [ ] Use dispose={null} for shared resources

### Poimandres Ecosystem

- [ ] Drei: useGLTF, useTexture, Environment, OrbitControls
- [ ] Zustand: Selectors, transient subscriptions
- [ ] Postprocessing: EffectComposer with SMAA
- [ ] Rapier: Simple colliders, collision events
- [ ] Leva: Hidden in production
