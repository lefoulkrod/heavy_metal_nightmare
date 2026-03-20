# Sprite Generation Prompts for Heavy Metal Nightmare

## Optimal Prompt Template

Use this template for generating game sprites that work well with the processing tools:

### Base Template
```
Pixel art sprite sheet showing [NUMBER] animation frames of a [CHARACTER DESCRIPTION]. 
Layout: [NUMBER] frames arranged horizontally in ONE row.
Frame size: [SIZE]x[SIZE] pixels each.
Background: Pure white (#FFFFFF) - NO SHADOWS under characters, NO GROUND, NO ENVIRONMENT.
Style: Heavy metal horror game aesthetic, retro pixel art.

Frames:
1. IDLE: [POSE DESCRIPTION]
2. [ACTION]1: [POSE DESCRIPTION]
3. [ACTION]2: [POSE DESCRIPTION]
4. [ACTION]: [POSE DESCRIPTION]

Requirements:
- Same character proportions in all frames
- Character centered in each frame
- NO text, NO watermarks, NO UI elements
- NO shadows, NO reflections, NO lighting effects
- White background only
```

## Player Character Prompt (80x80 frames)

```
Pixel art sprite sheet showing 4 animation frames of a heavy metal warrior player character.
Layout: 4 frames arranged horizontally in ONE row.
Frame size: 80x80 pixels each.
Background: Pure white (#FFFFFF) - NO SHADOWS under character, NO GROUND.

Character description:
- Male warrior with long hair
- Red/black armor with spikes
- Holding a glowing red guitar that doubles as an axe
- Heavy metal aesthetic

Frames:
1. IDLE: Standing still, guitar held at side
2. WALK1: Left leg forward, guitar held at hip
3. WALK2: Right leg forward, guitar held at hip
4. ATTACK: Guitar swung forward in arc, body twisted

Requirements:
- Same character size and center position in all frames
- Consistent proportions
- NO shadows, NO text, NO watermarks
- White background only
```

## Processing Workflow

1. Generate sprite sheet using the prompt above
2. Use `generate_and_process_sprites` tool with:
   - `size: "wide"` (for horizontal layouts)
   - `rows: 1`
   - `cols: 4`
   - `auto_detect: true`
   - `bg_color: "white"`
   - `clean_artifacts: true`

## Enemy Sprite Guidelines

All enemy sprites should be generated at their final render size:
- Player: 80x80
- Enemies: 80x80 (except Hell Knight which is 48x48)

Never upscale pixel art - generate at native resolution.

---

## Procedural Character Rigging System

For finer control over character design, use the **Rigging System** located in:
`/home/computron/generated_images/parts/`

### How It Works

Instead of generating complete sprites, this system uses:
1. **Individual components** (head, torso, arms, legs, hair, guitar)
2. **Anchor points** - pivot positions where parts connect
3. **Python composition scripts** - assemble poses from components

### Files Created

**Component Generators:**
- `build_v3.py` - Creates base components (head, torso, guitar, hair, arms, legs)
- `compose_v3.py` - Assembles 4 poses (idle, walk1, walk2, attack) from components

**Component Files:**
- `v3_head.png` - Character head with face
- `v3_hair_back.png` - Long flowing back hair
- `v3_hair_front.png` - Bangs (positioned high to show eyes)
- `v3_torso.png` - Black leather vest with studs
- `v3_guitar.png` - B.C. Rich style electric guitar
- `v3_arm_left.png` / `v3_arm_right.png` - Arms with bent joints
- `v3_leg.png` - Standing leg

**Final Poses:**
- `v3_idle.png` - Standing with guitar
- `v3_walk1.png` / `v3_walk2.png` - Walking animation
- `v3_attack.png` - Guitar swung up and forward

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Skin | `#F0C8B4` | Face, hands |
| Hair | `#C82828` | Main red hair |
| Hair Dark | `#961E1E` | Shadow/hair back |
| Hair Light | `#FF5050` | Highlights |
| Leather | `#2D2D2D` | Vest |
| Studs | `#C8C8D2` | Metal studs |
| Guitar | `#DC3232` | Guitar body |
| Guitar Dark | `#A02323` | Guitar shadows |
| Wood | `#A06E3C` | Guitar neck |
| Silver | `#DCDCE6` | Hardware |
| Boots | `#322823` | Footwear |

### Usage

To modify the character:

1. Edit `build_v3.py` to change colors, sizes, or add details
2. Run: `python3 build_v3.py` to regenerate components
3. Run: `python3 compose_v3.py` to rebuild poses
4. Copy final poses to game: `cp v3_*.png player_*.png`
5. Commit and push changes

### Current Player Character: Female Metal Warrior

**Design:** Long red hair, black leather vest, playing B.C. Rich guitar
**Resolution:** 80x80 pixels per frame
**Frames:** 4 (idle, walk1, walk2, attack)
**Status:** Live in production

