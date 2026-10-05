# events-stop-propagation

---

title: R3F pointer events pass through objects; stop them explicitly.
impact: MEDIUM

---

Unlike the DOM, an R3F event is not delivered only to the front-most object. The raycaster collects **every** intersected object with a handler and delivers the event to each of them, nearest first (and bubbles up each one's parents).

An object hidden behind another one still receives `onClick`, `onPointerOver`, etc.

## Bad Example

```jsx
// BAD - Clicking the front box also selects the box behind it
function Scene() {
  return (
    <>
      <mesh position={[0, 0, 1]} onClick={() => select("front")}>
        <boxGeometry />
        <meshStandardMaterial />
      </mesh>
      <mesh position={[0, 0, -1]} onClick={() => select("back")}>
        <boxGeometry />
        <meshStandardMaterial />
      </mesh>
    </>
  );
}
```

## Good Example

```jsx
// GOOD - The nearest hit stops the event; objects behind never get it
<mesh
  position={[0, 0, 1]}
  onClick={(e) => {
    e.stopPropagation();
    select("front");
  }}
>
```

`stopPropagation()` stops both directions:

- Objects further away along the ray
- Parent groups of the current object

Use it on hover too (`onPointerOver` / `onPointerOut`), otherwise a hovered object behind another one also shows its hover state.

## Notes

- While a pointer is captured (`e.target.setPointerCapture`), `stopPropagation()` only works on the capturing object.
- To make an object completely transparent to the raycaster (e.g. a glass panel in front of clickable objects), give it `raycast={() => null}`.
