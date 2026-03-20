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
