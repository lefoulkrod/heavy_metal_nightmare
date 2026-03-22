# Heavy Metal Warrior - Character Design Document

> **Reference document for sprite generation and rigging iterations**

---

## Character Overview

| Attribute | Description |
|-----------|-------------|
| **Name** | The Heavy Metal Warrior |
| **Gender** | Female |
| **Role** | Protagonist - Guitar Warrior |
| **Weapon** | Electric Guitar (BC Rich style) |
| **Genre** | Heavy Metal / Dark Fantasy |

---

## Visual Design

### Hair
- **Color:** Vibrant red
- **Style:** Long, flowing (reaches shoulders or mid-back)
- **Details:** May have volume/spikes for metal aesthetic

### Outfit
- **Primary Material:** Black leather
- **Style:** Metal/punk inspired
- **Details:**
  - Leather jacket or vest
  - Studs, spikes, or metal accents
  - Fingerless gloves
  - Combat boots
  - Optional: chains, buckles, patches

### Skin Tone
- Fair to medium (classic metal aesthetic)

---

## Weapon: The Guitar

### Style Reference
- **Model:** BC Rich Warlock or similar aggressive body shape
- **Body Shape:** Sharp, angular, pointed horns (distinctive BC Rich look)
- **Color:** Red (matching hair)
- **Details:**
  - Black hardware (tuners, bridge, pickups)
  - Silver/chrome accents
  - Sharp headstock shape
  - Multiple strings visible

### Guitar Positioning by Pose

#### Idle Pose
- Guitar held **horizontally across torso**
- As if being played (performance stance)
- Neck of guitar extends to the left
- Body of guitar rests against right hip/torso
- Both hands on guitar (playing position)

#### Walk Poses (1 & 2)
- Guitar remains **horizontal across torso**
- Slight bobbing motion with walk cycle
- Maintains playing position
- Legs alternate forward/back

#### Attack Pose (Wind-up)
- Guitar raised **HIGH above head**
- Held by the **neck** (headstock end)
- Body of guitar pointing **UP**
- Preparing for downward chop
- Arm extended back, ready to strike

#### Attack Pose (Strike)
- Guitar swung **DOWN in chopping motion**
- Still held by the **neck**
- Body of guitar now pointing **DOWN**
- Follow-through motion
- As if chopping with an axe

---

## Animation States

| State | Description | Guitar Position |
|-------|-------------|-----------------|
| **Idle** | Standing, breathing | Horizontal across torso |
| **Walk 1** | Left leg forward | Horizontal, slight bounce |
| **Walk 2** | Right leg forward | Horizontal, slight bounce |
| **Attack Wind-up** | Preparing to strike | Vertical, raised high |
| **Attack Strike** | Downward chop | Vertical, swung down |

---

## Color Palette

```
Primary Colors:
├── Hair: #CC0000 (Vibrant Red)
├── Guitar Body: #CC0000 (Matching Red)
├── Leather Outfit: #1A1A1A (Deep Black)
└── Skin: #FFDBAC (Fair)

Accent Colors:
├── Metal/Spikes: #C0C0C0 (Silver)
├── Guitar Hardware: #333333 (Dark Gray/Black)
├── Guitar Strings: #DDDDDD (Light Silver)
└── Highlights: #FF4444 (Bright Red)
```

---

## Rigging Notes

### Joint Hierarchy
```
torso (root)
├── neck → head
├── shoulder_left → left_arm
│   ├── elbow_left → (no child, cosmetic)
│   └── wrist_left → guitar (ATTACHMENT POINT)
├── shoulder_right → right_arm
│   ├── elbow_right
│   └── wrist_right
├── hip_left → left_leg
│   └── knee_left
└── hip_right → right_leg
    └── knee_right
```

### Key Rigging Points
1. **Guitar attaches to LEFT WRIST** - This allows the guitar to follow hand motion during attacks
2. **Guitar pivot point** should be at the neck/headstock junction
3. **Attack animation** requires full arm rotation from shoulder through wrist
4. **Horizontal poses** use cumulative angles to achieve -90° (horizontal)
5. **Vertical poses** use 0° or -180° depending on direction

---

## Future Iterations Checklist

- [ ] Update hair color to red
- [ ] Change outfit to black leather
- [ ] Redesign guitar to BC Rich style (red, angular)
- [ ] Verify horizontal guitar position for idle/walk
- [ ] Verify chopping motion for attack poses
- [ ] Add female body proportions
- [ ] Add leather texture details
- [ ] Add metal studs/spikes
- [ ] Consider adding face paint or tattoos
- [ ] Add chain accessories

---

## Reference Images

*Note: Add reference images here when available*

### BC Rich Guitar Style
- Sharp, angular body with pointed horns
- Aggressive, weapon-like appearance
- Distinctive headstock shape

### Metal Fashion References
- Black leather jackets
- Studded accessories
- Combat boots
- Fingerless gloves

---

## Technical Specifications

- **Canvas Size:** 200x250 pixels
- **Style:** Pixel art
- **Format:** PNG with transparency
- **Animation Frames:** 
  - Idle: 1 frame
  - Walk: 2 frames (cycle)
  - Attack: 2 frames (wind-up, strike)

---

*Last Updated: 2025*
*Document Version: 1.0*
