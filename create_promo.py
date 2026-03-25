#!/usr/bin/env python3
"""Create a promotional sprite sheet image for Heavy Metal Nightmare."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

# Paths
SPRITE_PATH = 'sprites_metal_warrior/player_spritesheet.png'
OUTPUT_PATH = 'promo_image.png'

# Load the sprite sheet
sprite_sheet = Image.open(SPRITE_PATH).convert('RGBA')
sheet_width, sheet_height = sprite_sheet.size

# Calculate individual sprite dimensions (5 sprites in a row)
num_sprites = 5
sprite_width = sheet_width // num_sprites
sprite_height = sheet_height

print(f"Sprite sheet: {sheet_width}x{sheet_height}")
print(f"Individual sprite: {sprite_width}x{sprite_height}")

# Create the promotional image
promo_width = 1200
promo_height = 600
promo = Image.new('RGBA', (promo_width, promo_height), (0, 0, 0, 255))
draw = ImageDraw.Draw(promo)

# Create dark red to black gradient background
for y in range(promo_height):
    # Gradient from dark red at top to black at bottom
    ratio = y / promo_height
    # Start with dark red, fade to black
    r = int(80 * (1 - ratio * 0.7))
    g = 0
    b = int(20 * (1 - ratio * 0.5))
    draw.line([(0, y), (promo_width, y)], fill=(r, g, b, 255))

# Add some red glow at the top
for y in range(100):
    alpha = int(60 * (1 - y / 100))
    for x in range(promo_width):
        current = promo.getpixel((x, y))
        new_r = min(255, current[0] + alpha)
        promo.putpixel((x, y), (new_r, current[1], current[2], 255))

# Extract and place sprites
sprite_spacing = 200
start_x = (promo_width - (num_sprites * sprite_spacing)) // 2
sprite_y = promo_height - sheet_height - 80  # Position sprites near bottom

for i in range(num_sprites):
    # Extract sprite
    left = i * sprite_width
    right = left + sprite_width
    sprite = sprite_sheet.crop((left, 0, right, sprite_height))
    
    # Scale up slightly for better visibility
    scale = 1.5
    new_width = int(sprite_width * scale)
    new_height = int(sprite_height * scale)
    sprite = sprite.resize((new_width, new_height), Image.NEAREST)
    
    # Calculate position
    x_pos = start_x + i * sprite_spacing - (new_width - sprite_width) // 2
    y_pos = sprite_y - (new_height - sprite_height)
    
    # Add drop shadow effect
    shadow = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rectangle((5, 5, new_width, new_height), fill=(0, 0, 0, 100))
    
    # Paste sprite with shadow
    promo.paste(shadow, (x_pos, y_pos), shadow)
    promo.paste(sprite, (x_pos, y_pos), sprite)

# Try to load a bold font, fall back to default
try:
    # Try common bold fonts
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',
    ]
    title_font = None
    for fp in font_paths:
        if os.path.exists(fp):
            title_font = ImageFont.truetype(fp, 60)
            subtitle_font = ImageFont.truetype(fp, 28)
            break
    if title_font is None:
        raise FileNotFoundError("No bold font found")
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Draw title text with metallic effect
title = "HEAVY METAL NIGHTMARE"
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (promo_width - title_width) // 2
title_y = 40

# Draw text shadow
draw.text((title_x + 3, title_y + 3), title, font=title_font, fill=(0, 0, 0, 200))
# Draw main text in metallic red
draw.text((title_x, title_y), title, font=title_font, fill=(200, 30, 30, 255))
# Draw highlight
draw.text((title_x - 1, title_y - 1), title, font=title_font, fill=(255, 100, 100, 100))

# Draw subtitle
subtitle = "NEW PLAYER CHARACTER UPDATE"
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (promo_width - subtitle_width) // 2
subtitle_y = promo_height - 50

# Subtitle with glow effect
draw.text((subtitle_x + 2, subtitle_y + 2), subtitle, font=subtitle_font, fill=(100, 0, 0, 200))
draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill=(255, 200, 200, 255))

# Add decorative lines
draw.line([(100, 110), (promo_width - 100, 110)], fill=(150, 30, 30, 200), width=2)
draw.line([(100, 115), (promo_width - 100, 115)], fill=(80, 10, 10, 150), width=1)

# Add some sparkle/glow effects around sprites
for i in range(num_sprites):
    x_center = start_x + i * sprite_spacing + sprite_width // 2
    y_center = sprite_y + sprite_height // 2
    
    # Add subtle glow behind each sprite
    for radius in range(30, 5, -5):
        alpha = int(20 * (30 - radius) / 25)
        glow_color = (150, 30, 30, alpha)
        draw.ellipse([
            x_center - radius, y_center - radius,
            x_center + radius, y_center + radius
        ], fill=None, outline=glow_color, width=1)

# Add sprite labels
label_font = ImageFont.load_default()
try:
    label_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
except:
    pass

labels = ['IDLE', 'WALK 1', 'WALK 2', 'ATTACK\nWINDUP', 'ATTACK\nSTRIKE']
for i, label in enumerate(labels):
    x_pos = start_x + i * sprite_spacing + sprite_width // 2 - 30
    y_pos = sprite_y + sheet_height + 10
    lines = label.split('\n')
    for j, line in enumerate(lines):
        text_bbox = draw.textbbox((0, 0), line, font=label_font)
        text_width = text_bbox[2] - text_bbox[0]
        draw.text((x_pos + (60 - text_width) // 2, y_pos + j * 16), line, 
                  font=label_font, fill=(200, 150, 150, 255))

# Apply a subtle vignette effect
vignette = Image.new('RGBA', (promo_width, promo_height), (0, 0, 0, 0))
vignette_draw = ImageDraw.Draw(vignette)

# Darken edges
for i in range(50):
    alpha = int(100 * i / 50)
    vignette_draw.rectangle(
        [i, i, promo_width - i, promo_height - i],
        outline=(0, 0, 0, alpha),
        width=1
    )

promo = Image.alpha_composite(promo, vignette)

# Convert to RGB for saving as PNG
promo_rgb = Image.new('RGB', (promo_width, promo_height), (0, 0, 0))
promo_rgb.paste(promo, mask=promo.split()[3])

# Save the promotional image
promo_rgb.save(OUTPUT_PATH, 'PNG')
print(f"Promotional image saved to {OUTPUT_PATH}")
print(f"Size: {promo_width}x{promo_height}")