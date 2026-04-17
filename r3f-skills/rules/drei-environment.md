# drei-environment

---

title: Use Environment for realistic lighting.
impact: MEDIUM-HIGH

---

```jsx
import { Environment } from '@react-three/drei';

// Preset environments
<Environment preset="city" /> // apartment, city, dawn, forest, lobby, night, park, studio, sunset, warehouse

// Custom HDR
<Environment files="/env.hdr" />

// Background visible
<Environment background preset="sunset" />

// Ground projection
<Environment ground={{ height: 15, radius: 60 }} preset="city" />
```
