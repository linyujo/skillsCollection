# events-event-data

---

title: Understand event data structure.
impact: MEDIUM

---

```jsx
<mesh onClick={(event) => {
  // event contains:
  event.object;      // The mesh that was clicked
  event.eventObject; // The object that has the event handler
  event.point;       // World position of click (Vector3)
  event.distance;    // Distance from camera
  event.ray;         // The ray used for intersection
  event.camera;      // Camera used for raycasting
  event.uv;          // UV coordinates at intersection
  event.face;        // Face that was hit
  event.faceIndex;   // Index of hit face
  event.delta;       // Distance traveled since pointer down (for drag detection)
  event.stopPropagation(); // Stop bubbling
  event.nativeEvent; // Original DOM event
}}>
```
