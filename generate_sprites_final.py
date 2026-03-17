#!/usr/bin/env python3
"""
Heavy Metal Nightmare - Final Player Character Sprite Generator
Highly detailed metal warrior with unique visual identity
"""

from PIL import Image, ImageDraw

def create_metal_warrior(pose="idle"):
    """Create detailed 80x80 metal warrior sprite"""
    img = Image.new('RGBA', (80, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Enhanced color palette - distinct from common game characters
    SKIN = (195, 145, 105)
    SKIN_SHADE = (155, 105, 65)
    HAIR = (15, 15, 20)
    HAIR_HIGH = (40, 40, 50)
    ARMOR_BASE = (45, 45, 65)
    ARMOR_LIGHT = (85, 85, 110)
    ARMOR_BRIGHT = (180, 180, 200)
    CHROME = (220, 220, 235)
    SPIKE = (240, 240, 255)
    EYE_RED = (255, 20, 20)
    EYE_CORE = (255, 150, 100)
    GUITAR_BODY = (160, 40, 40)
    GUITAR_DARK = (100, 25, 25)
    GUITAR_EDGE = (200, 60, 60)
    FRETBOARD = (90, 70, 50)
    GOLD = (255, 220, 80)
    DARK = (25, 25, 35)
    BOOT = (55, 55, 70)
    
    # Position based on pose
    if pose == "idle":
        cx, base_y = 38, 72
        lean = 0
        l_leg = [(cx-6, base_y-18), (cx-8, base_y-5), (cx-4, base_y), (cx-2, base_y-18)]
        r_leg = [(cx+2, base_y-18), (cx, base_y-5), (cx+4, base_y), (cx+6, base_y-18)]
        l_boot = [(cx-10, base_y-5), (cx-2, base_y-5), (cx, base_y), (cx-10, base_y)]
        r_boot = [(cx-2, base_y-5), (cx+6, base_y-5), (cx+8, base_y), (cx-2, base_y)]
        spike_x = cx+5
        arm_r_pos = (cx+12, base_y-20)
        guitar_rot = 0
    
    elif pose == "attack":
        cx, base_y = 42, 70
        lean = -3
        # Wide stance
        l_leg = [(cx-10, base_y-16), (cx-18, base_y-5), (cx-12, base_y), (cx-4, base_y-16)]
        r_leg = [(cx+2, base_y-16), (cx+10, base_y-5), (cx+18, base_y), (cx+6, base_y-16)]
        l_boot = [(cx-20, base_y-5), (cx-10, base_y-5), (cx-8, base_y), (cx-20, base_y)]
        r_boot = [(cx+8, base_y-5), (cx+20, base_y-5), (cx+24, base_y), (cx+8, base_y)]
        spike_x = cx+18
        arm_r_pos = (cx+25, base_y-35)
        guitar_rot = -40
    
    elif pose == "walk1":
        cx, base_y = 36, 71
        lean = 2
        # Left back, right forward
        l_leg = [(cx-6, base_y-17), (cx-10, base_y-5), (cx-6, base_y), (cx-2, base_y-17)]
        r_leg = [(cx+2, base_y-17), (cx+10, base_y-5), (cx+16, base_y), (cx+6, base_y-17)]
        l_boot = [(cx-12, base_y-5), (cx-4, base_y-5), (cx-2, base_y), (cx-12, base_y)]
        r_boot = [(cx+7, base_y-5), (cx+19, base_y-5), (cx+22, base_y), (cx+7, base_y)]
        spike_x = cx+16
        arm_r_pos = (cx+8, base_y-15)
        guitar_rot = 15
    
    else:  # walk2
        cx, base_y = 36, 71
        lean = 2
        # Left forward, right back
        l_leg = [(cx-4, base_y-17), (cx+2, base_y-5), (cx+6, base_y), (cx+2, base_y-17)]
        r_leg = [(cx+2, base_y-17), (cx-2, base_y-5), (cx+2, base_y), (cx+6, base_y-17)]
        l_boot = [(cx, base_y-5), (cx+10, base_y-5), (cx+12, base_y), (cx, base_y)]
        r_boot = [(cx-4, base_y-5), (cx+4, base_y-5), (cx+6, base_y), (cx-4, base_y)]
        spike_x = cx+8
        arm_r_pos = (cx+14, base_y-22)
        guitar_rot = -10
    
    # ========== LEGS ==========
    # Left leg (back)
    draw.polygon(l_leg, fill=ARMOR_BASE, outline=DARK)
    draw.polygon(l_boot, fill=BOOT, outline=CHROME)
    
    # Right leg (front)
    draw.polygon(r_leg, fill=ARMOR_LIGHT, outline=DARK)
    draw.polygon(r_boot, fill=BOOT, outline=CHROME)
    # Boot spike
    draw.polygon([(spike_x, base_y-8), (spike_x+6, base_y-15), (spike_x+3, base_y-5)], 
                fill=SPIKE, outline=DARK)
    
    # ========== TORSO ==========
    ty = base_y - 18  # Torso Y start
    
    # Main body
    body_pts = [(cx-9+lean, ty), (cx-11+lean, ty-26), (cx+11+lean, ty-26), (cx+9+lean, ty)]
    draw.polygon(body_pts, fill=ARMOR_BASE, outline=DARK)
    
    # Chest plate with chrome finish
    chest_pts = [(cx-8+lean, ty-3), (cx-9+lean, ty-23), (cx+9+lean, ty-23), (cx+8+lean, ty-3)]
    draw.polygon(chest_pts, fill=ARMOR_BRIGHT, outline=DARK)
    
    # Inverted cross (metal symbol)
    draw.line([(cx+lean, ty-21), (cx+lean, ty-6)], fill=DARK, width=3)
    draw.line([(cx-4+lean, ty-13), (cx+4+lean, ty-13)], fill=DARK, width=2)
    draw.line([(cx-3+lean, ty-6), (cx+3+lean, ty-6)], fill=GUITAR_BODY, width=2)
    
    # Chrome rivets on chest
    for rx in range(cx-5+lean, cx+6+lean, 4):
        draw.ellipse([(rx-1, ty-19), (rx+1, ty-17)], fill=CHROME, outline=DARK)
        draw.ellipse([(rx-1, ty-10), (rx+1, ty-8)], fill=CHROME, outline=DARK)
    
    # Belt with skull buckle
    draw.rectangle([(cx-10+lean, ty), (cx+10+lean, ty+5)], fill=DARK, outline=CHROME)
    # Skull buckle
    draw.ellipse([(cx-3+lean, ty+1), (cx+3+lean, ty+4)], fill=CHROME, outline=DARK)
    draw.line([(cx+lean, ty+2), (cx+lean, ty+4)], fill=DARK, width=1)
    # Belt spikes
    draw.polygon([(cx-8+lean, ty), (cx-6+lean, ty-5), (cx-4+lean, ty)], fill=SPIKE, outline=DARK)
    draw.polygon([(cx+4+lean, ty), (cx+6+lean, ty-5), (cx+8+lean, ty)], fill=SPIKE, outline=DARK)
    
    # ========== SHOULDER PADS ==========
    # Left (back)
    draw.ellipse([(cx-17+lean, ty-22), (cx-7+lean, ty-12)], fill=ARMOR_LIGHT, outline=DARK)
    draw.polygon([(cx-15+lean, ty-22), (cx-13+lean, ty-28), (cx-11+lean, ty-22)], 
                fill=SPIKE, outline=DARK)
    
    # Right (front - larger, more spikes)
    draw.ellipse([(cx+5+lean, ty-24), (cx+17+lean, ty-12)], fill=ARMOR_LIGHT, outline=DARK)
    draw.polygon([(cx+7+lean, ty-24), (cx+9+lean, ty-30), (cx+11+lean, ty-24)], 
                fill=SPIKE, outline=DARK)
    draw.polygon([(cx+11+lean, ty-23), (cx+13+lean, ty-29), (cx+15+lean, ty-23)], 
                fill=SPIKE, outline=DARK)
    draw.polygon([(cx+13+lean, ty-21), (cx+15+lean, ty-27), (cx+17+lean, ty-21)], 
                fill=SPIKE, outline=DARK)
    
    # ========== HEAD ==========
    hy = ty - 24  # Head Y
    
    # Neck
    draw.rectangle([(cx-3+lean, hy+5), (cx+3+lean, hy+10)], fill=SKIN_SHADE, outline=DARK)
    
    # Face (profile)
    draw.ellipse([(cx-6+lean, hy-6), (cx+6+lean, hy+8)], fill=SKIN, outline=DARK)
    
    # Nose
    draw.polygon([(cx+4+lean, hy), (cx+7+lean, hy+1), (cx+4+lean, hy+2)], 
                fill=SKIN_SHADE, outline=DARK)
    
    # Glowing red eye with intensity
    # Outer glow
    for r in range(4, 0, -1):
        intensity = 60 if r == 4 else 100 if r == 3 else 150 if r == 2 else 255
        color = (255, intensity//4, intensity//4)
        draw.ellipse([(cx+lean-r, hy-3-r), (cx+4+lean+r, hy+1+r)], fill=color)
    # Eye core
    draw.ellipse([(cx+lean, hy-2), (cx+4+lean, hy+2)], fill=EYE_RED, outline=DARK)
    draw.ellipse([(cx+1+lean, hy-1), (cx+3+lean, hy+1)], fill=EYE_CORE, outline=DARK)
    draw.point([(cx+2+lean, hy)], fill=(255, 255, 255))
    
    # Mouth (grim line)
    draw.line([(cx+2+lean, hy+4), (cx+5+lean, hy+4)], fill=DARK, width=1)
    
    # ========== HAIR (Long flowing black) ==========
    # Top of head
    draw.ellipse([(cx-7+lean, hy-10), (cx+5+lean, hy-2)], fill=HAIR, outline=DARK)
    
    # Flowing back hair - multiple strands
    hair_main = [
        (cx-5+lean, hy-2), (cx-12+lean, hy+5),
        (cx-15+lean, hy+20), (cx-11+lean, hy+35),
        (cx-6+lean, hy+42), (cx-2+lean, hy+36),
        (cx+lean, hy+26), (cx+2+lean, hy+38),
        (cx+6+lean, hy+30), (cx+4+lean, hy+12),
        (cx+2+lean, hy+2), (cx-2+lean, hy-2)
    ]
    draw.polygon(hair_main, fill=HAIR, outline=DARK)
    
    # Hair shine/highlight
    draw.line([(cx-7+lean, hy+2), (cx-10+lean, hy+18)], fill=HAIR_HIGH, width=2)
    draw.line([(cx+lean, hy+5), (cx+3+lean, hy+22)], fill=HAIR_HIGH, width=2)
    
    # Front bangs
    draw.polygon([(cx-5+lean, hy-6), (cx-3+lean, hy+3), (cx-1+lean, hy-5)], 
                fill=HAIR, outline=DARK)
    draw.polygon([(cx+1+lean, hy-5), (cx+3+lean, hy+3), (cx+5+lean, hy-6)], 
                fill=HAIR, outline=DARK)
    
    # ========== LEFT ARM (Back) ==========
    if pose == "attack":
        # Raised back
        draw.polygon([
            (cx-9+lean, ty-18), (cx-20+lean, ty-28),
            (cx-22+lean, ty-20), (cx-11+lean, ty-12)
        ], fill=ARMOR_BASE, outline=DARK)
        draw.ellipse([(cx-24+lean, ty-31), (cx-16+lean, ty-23)], fill=SKIN, outline=DARK)
        # Spiked bracer
        draw.rectangle([(cx-22+lean, ty-28), (cx-16+lean, ty-22)], fill=DARK, outline=CHROME)
        draw.polygon([(cx-20+lean, ty-28), (cx-18+lean, ty-33), (cx-16+lean, ty-28)], 
                    fill=SPIKE, outline=DARK)
    else:
        # Normal position
        draw.polygon([
            (cx-9+lean, ty-18), (cx-15+lean, ty+2),
            (cx-11+lean, ty+6), (cx-5+lean, ty-12)
        ], fill=ARMOR_BASE, outline=DARK)
        draw.ellipse([(cx-17+lean, ty), (cx-9+lean, ty+8)], fill=SKIN, outline=DARK)
        draw.rectangle([(cx-15+lean, ty+2), (cx-9+lean, ty+6)], fill=DARK, outline=CHROME)
    
    # ========== RIGHT ARM (Front with Guitar) ==========
    if pose == "attack":
        # Swinging guitar high
        draw.polygon([
            (cx+10+lean, ty-18), (cx+30+lean, ty-38),
            (cx+34+lean, ty-30), (cx+14+lean, ty-12)
        ], fill=ARMOR_LIGHT, outline=DARK)
        draw.ellipse([(cx+28+lean, ty-42), (cx+36+lean, ty-34)], fill=SKIN, outline=DARK)
        
        # GUITAR - Swung up for attack
        gx, gy = cx+32+lean, ty-45
        
        # Guitar body (distinctive shape)
        g_body = [
            (gx, gy), (gx+22, gy-8),
            (gx+28, gy+12), (gx+18, gy+22),
            (gx+8, gy+17), (gx-2, gy+7)
        ]
        draw.polygon(g_body, fill=GUITAR_BODY, outline=DARK)
        # Body detail - pickup
        draw.ellipse([(gx+6, gy-3), (gx+16, gy+7)], outline=GUITAR_EDGE, width=2)
        draw.rectangle([(gx+8, gy-1), (gx+14, gy+5)], fill=CHROME, outline=DARK)
        
        # Neck extended
        draw.polygon([
            (gx+18, gy-8), (gx+48, gy-30),
            (gx+52, gy-24), (gx+22, gy-2)
        ], fill=FRETBOARD, outline=DARK)
        
        # Frets
        for i in range(5):
            fy = gy - 10 - i*4
            fx = gx + 22 + i*6
            draw.line([(fx, fy), (fx+3, fy-2)], fill=CHROME, width=1)
        
        # Headstock
        draw.polygon([
            (gx+46, gy-32), (gx+60, gy-42),
            (gx+64, gy-35), (gx+52, gy-26)
        ], fill=DARK, outline=GOLD)
        
        # Tuning pegs
        draw.ellipse([(gx+54, gy-38), (gx+57, gy-35)], fill=GOLD, outline=DARK)
        draw.ellipse([(gx+58, gy-35), (gx+61, gy-32)], fill=GOLD, outline=DARK)
        
        # Blade edge (battle axe)
        draw.polygon([
            (gx+22, gy-18), (gx+42, gy-48),
            (gx+32, gy+5)
        ], fill=CHROME, outline=DARK)
        # Blade edge highlight
        draw.line([(gx+28, gy-20), (gx+38, gy-38)], fill=SPIKE, width=2)
        
        # Strings
        for i in range(3):
            off = i * 3
            draw.line([(gx+20+off, gy-5), (gx+46+off, gy-26)], fill=GOLD, width=1)
    
    elif pose in ["walk1", "walk2"]:
        # Walking arm position
        ax, ay = arm_r_pos
        
        draw.polygon([
            (cx+10+lean, ty-18), (ax, ay+5),
            (ax+4, ay+9), (cx+14+lean, ty-12)
        ], fill=ARMOR_LIGHT, outline=DARK)
        draw.ellipse([(ax-2, ay+3), (ax+6, ay+11)], fill=SKIN, outline=DARK)
        
        # Guitar at side
        gx, gy = ax, ay
        g_body = [
            (gx, gy), (gx+20, gy-5),
            (gx+25, gy+15), (gx+15, gy+25),
            (gx+5, gy+20), (gx-5, gy+10)
        ]
        draw.polygon(g_body, fill=GUITAR_BODY, outline=DARK)
        draw.ellipse([(gx+6, gy+5), (gx+16, gy+15)], outline=GUITAR_EDGE, width=2)
        
        # Neck pointing down
        draw.polygon([
            (gx+15, gy+8), (gx+28, gy+38),
            (gx+33, gy+35), (gx+20, gy+6)
        ], fill=FRETBOARD, outline=DARK)
        
        # Headstock
        draw.polygon([
            (gx+26, gy+40), (gx+38, gy+48),
            (gx+42, gy+42), (gx+32, gy+35)
        ], fill=DARK, outline=GOLD)
        
        # Blade
        draw.polygon([
            (gx+20, gy+2), (gx+38, gy-18),
            (gx+28, gy+22)
        ], fill=CHROME, outline=DARK)
        draw.line([(gx+26, gy), (gx+34, gy-12)], fill=SPIKE, width=2)
    
    else:  # idle
        # Ready position
        draw.polygon([
            (cx+10+lean, ty-18), (cx+26+lean, ty-8),
            (cx+30+lean, ty-3), (cx+14+lean, ty-12)
        ], fill=ARMOR_LIGHT, outline=DARK)
        draw.ellipse([(cx+24+lean, ty-11), (cx+32+lean, ty-3)], fill=SKIN, outline=DARK)
        
        # Guitar ready
        gx, gy = cx+28+lean, ty-8
        g_body = [
            (gx, gy), (gx+22, gy-5),
            (gx+27, gy+15), (gx+17, gy+25),
            (gx+7, gy+20), (gx-3, gy+10)
        ]
        draw.polygon(g_body, fill=GUITAR_BODY, outline=DARK)
        draw.ellipse([(gx+7, gy+5), (gx+17, gy+15)], outline=GUITAR_EDGE, width=2)
        # Bridge
        draw.rectangle([(gx+10, gy+8), (gx+16, gy+12)], fill=CHROME, outline=DARK)
        
        # Neck
        draw.polygon([
            (gx+17, gy+8), (gx+38, gy-12),
            (gx+43, gy-7), (gx+22, gy+13)
        ], fill=FRETBOARD, outline=DARK)
        
        # Frets
        for i in range(4):
            fx = gx + 20 + i*5
            fy = gy - 2 - i*4
            draw.line([(fx, fy), (fx+2, fy-1)], fill=CHROME, width=1)
        
        # Headstock
        draw.polygon([
            (gx+36, gy-15), (gx+52, gy-25),
            (gx+56, gy-18), (gx+42, gy-10)
        ], fill=DARK, outline=GOLD)
        
        # Tuning pegs
        draw.ellipse([(gx+44, gy-20), (gx+47, gy-17)], fill=GOLD, outline=DARK)
        draw.ellipse([(gx+48, gy-17), (gx+51, gy-14)], fill=GOLD, outline=DARK)
        
        # Blade
        draw.polygon([
            (gx+22, gy-5), (gx+44, gy-32),
            (gx+34, gy+10)
        ], fill=CHROME, outline=DARK)
        draw.line([(gx+28, gy-8), (gx+40, gy-26)], fill=SPIKE, width=2)
        
        # Strings
        for i in range(3):
            off = i * 2
            draw.line([(gx+20+off, gy), (gx+38+off, gy-17)], fill=GOLD, width=1)
    
    # ========== CHAIN MAIL DETAIL ==========
    for y in range(ty-20, ty-5, 3):
        for x in range(cx-5+lean, cx+6+lean, 2):
            draw.ellipse([(x-1, y-1), (x+1, y+1)], outline=ARMOR_LIGHT)
    
    return img

def main():
    poses = {
        "player_idle.png": "idle",
        "player_attack.png": "attack",
        "player_walk1.png": "walk1",
        "player_walk2.png": "walk2"
    }
    
    output_dir = "/home/computron/heavy_metal_nightmare/"
    
    print("=" * 60)
    print("HEAVY METAL NIGHTMARE - Player Sprite Generator")
    print("=" * 60)
    print("\nGenerating high-fidelity metal warrior sprites...\n")
    
    for filename, pose in poses.items():
        print(f"  Creating {filename}...", end=" ")
        sprite = create_metal_warrior(pose)
        filepath = output_dir + filename
        sprite.save(filepath, "PNG")
        print("✓")
    
    print("\n" + "=" * 60)
    print("SPRITES COMPLETE!")
    print("=" * 60)
    print("\nOutput files:")
    for filename in poses.keys():
        print(f"  • {output_dir}{filename}")
    
    print("\nSprite specifications:")
    print("  • Dimensions: 80x80 pixels")
    print("  • Format: PNG with alpha transparency")
    print("  • Style: Side-view 2D platformer")
    print("  • Character: Dark fantasy metal warrior")
    print("  • Features:")
    print("    - Long flowing black hair")
    print("    - Spiked leather armor")
    print("    - Electric guitar battle axe")
    print("    - Glowing red eyes")
    print("    - Chrome/silver accents")
    print("    - Chain mail details")
    print("\nAnimation frames:")
    print("  1. player_idle.png   - Standing ready pose")
    print("  2. player_attack.png - Guitar swing attack")
    print("  3. player_walk1.png  - Walking frame 1")
    print("  4. player_walk2.png  - Walking frame 2")

if __name__ == "__main__":
    main()
