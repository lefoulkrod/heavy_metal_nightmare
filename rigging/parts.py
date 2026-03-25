"""
Part definitions for the Metal Warrior character.
Heavy Metal Warrior - Female character with BC Rich Warlock guitar
"""

from PIL import Image, ImageDraw
from typing import Tuple
import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
from core.part import Part


# Heavy Metal Warrior color palette
METAL_COLORS = {
    'black_leather': (26, 26, 26),      # #1A1A1A - torso
    'dark_leather': (40, 30, 30),
    'brown_leather': (80, 50, 30),
    'silver': (192, 192, 192),          # #C0C0C0 - accents
    'dark_silver': (120, 130, 140),
    'gold': (200, 170, 80),
    'skin': (255, 219, 172),            # #FFDBAC - fair skin
    'black': (20, 20, 25),
    'vibrant_red': (204, 0, 0),         # #CC0000 - hair and guitar
    'black_hardware': (51, 51, 51),     # #333333 - guitar hardware
    'red_accent': (180, 30, 30),
}


def create_guitar(
    name: str = "guitar",
    body_width: int = 50,
    body_height: int = 70,
    neck_length: int = 60,
    body_color: Tuple[int, int, int] = METAL_COLORS['vibrant_red'],
    neck_color: Tuple[int, int, int] = (30, 30, 30),
    accent_color: Tuple[int, int, int] = METAL_COLORS['silver'],
    pivot_at_neck: bool = False
) -> Part:
    """Create a BC Rich Warlock style guitar - sharp, angular, weapon-like.
    
    Args:
        name: Part name
        body_width: Width of guitar body
        body_height: Height of guitar body
        neck_length: Length of neck/headstock
        body_color: Main body color
        neck_color: Neck/headstock color
        accent_color: Accent color for hardware
        pivot_at_neck: If True, pivot at neck/headstock (for attack poses).
                      If False, pivot at body (for playing/idle poses).
    """
    total_height = body_height + neck_length
    total_width = body_width + 30  # Extra width for the angular horns
    
    # Set pivot based on usage
    if pivot_at_neck:
        # Pivot at neck/headstock - hand grips here for attack
        pivot_x = 0.5
        pivot_y = 0.15  # Near top where headstock is
    else:
        # Pivot at body - rests against torso for playing
        pivot_x = 0.5
        pivot_y = 0.7  # Near body center
    
    part = Part(
        name=name,
        width=total_width,
        height=total_height,
        pivot_x=pivot_x,
        pivot_y=pivot_y,
        color=body_color
    )
    
    def create_guitar_image():
        img = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx = total_width // 2
        neck_top = 5
        body_top = neck_length
        body_bottom = total_height - 5
        
        # Guitar neck (black)
        neck_width = 14
        draw.rectangle(
            [cx - neck_width//2, neck_top, cx + neck_width//2, body_top + 15],
            fill=neck_color,
            outline=METAL_COLORS['black_hardware'],
            width=2
        )
        
        # Frets on neck (silver)
        for i in range(1, 10):
            fret_y = neck_top + i * (body_top - neck_top) // 10
            draw.line([(cx - neck_width//2, fret_y), (cx + neck_width//2, fret_y)],
                     fill=METAL_COLORS['silver'], width=1)
        
        # BC Rich Warlock body - sharp angular shape with pointed horns
        # Upper horns (pointed, aggressive)
        upper_left_horn = [
            (cx - 5, body_top + 5),
            (cx - body_width//2 - 10, body_top - 5),
            (cx - body_width//3, body_top + 15)
        ]
        upper_right_horn = [
            (cx + 5, body_top + 5),
            (cx + body_width//2 + 10, body_top - 5),
            (cx + body_width//3, body_top + 15)
        ]
        
        # Main body - angular V-shape
        body_points = [
            (cx - body_width//2 - 5, body_top + 10),   # Upper left
            (cx - body_width//3, body_top + body_height//3),  # Left waist
            (cx - body_width//2, body_bottom - 15),    # Lower left horn tip
            (cx, body_bottom - 5),                      # Bottom center
            (cx + body_width//2, body_bottom - 15),    # Lower right horn tip
            (cx + body_width//3, body_top + body_height//3),  # Right waist
            (cx + body_width//2 + 5, body_top + 10),   # Upper right
            (cx + 5, body_top + 5),                   # Back to neck right
            (cx - 5, body_top + 5),                   # Back to neck left
        ]
        
        # Draw main body
        draw.polygon(body_points, fill=body_color, 
                    outline=METAL_COLORS['black_hardware'], width=3)
        
        # Draw upper horns
        draw.polygon(upper_left_horn, fill=body_color, 
                    outline=METAL_COLORS['black_hardware'], width=2)
        draw.polygon(upper_right_horn, fill=body_color, 
                    outline=METAL_COLORS['black_hardware'], width=2)
        
        # Bridge (black hardware)
        bridge_y = body_top + body_height * 2 // 3
        draw.rectangle(
            [cx - 15, bridge_y - 4, cx + 15, bridge_y + 4],
            fill=METAL_COLORS['black_hardware'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Dual humbucker pickups (black)
        pickup1_y = body_top + body_height // 3
        pickup2_y = body_top + body_height // 2
        for py in [pickup1_y, pickup2_y]:
            draw.rectangle(
                [cx - 12, py - 5, cx + 12, py + 5],
                fill=METAL_COLORS['black_hardware'],
                outline=METAL_COLORS['silver'],
                width=2
            )
            # Pickup poles
            for i in range(-2, 3):
                pole_x = cx + i * 5
                draw.ellipse([pole_x - 2, py - 3, pole_x + 2, py + 3], 
                           fill=METAL_COLORS['silver'])
        
        # Volume/tone knobs (silver)
        for i, kx in enumerate([cx - 10, cx + 10]):
            ky = body_bottom - 25 + i * 3
            draw.ellipse([kx - 4, ky - 4, kx + 4, ky + 4], 
                        fill=METAL_COLORS['silver'],
                        outline=METAL_COLORS['black_hardware'], width=1)
        
        # Sharp metal spikes on body (silver accents)
        spike_positions = [
            (cx - body_width//2 - 5, body_top + 15),
            (cx + body_width//2 + 5, body_top + 15),
            (cx - body_width//2, body_bottom - 15),
            (cx + body_width//2, body_bottom - 15),
        ]
        for sx, sy in spike_positions:
            draw.polygon(
                [(sx, sy - 8), (sx - 4, sy + 3), (sx + 4, sy + 3)],
                fill=accent_color,
                outline=METAL_COLORS['dark_silver']
            )
        
        # Guitar strings (silver)
        for i in range(-2, 3):
            string_x = cx + i * 2
            draw.line(
                [(string_x, neck_top + 5), (string_x, bridge_y)],
                fill=METAL_COLORS['silver'],
                width=1
            )
        
        # Headstock (pointed Warlock style)
        headstock_points = [
            (cx - neck_width//2, neck_top),
            (cx - neck_width, neck_top - 15),
            (cx, neck_top - 20),
            (cx + neck_width, neck_top - 15),
            (cx + neck_width//2, neck_top)
        ]
        draw.polygon(headstock_points, fill=body_color,
                    outline=METAL_COLORS['black_hardware'], width=2)
        
        # Tuning pegs
        for i in range(3):
            # Left side
            peg_y = neck_top - 5 - i * 5
            draw.ellipse([cx - neck_width - 3, peg_y - 2, cx - neck_width + 3, peg_y + 2],
                        fill=METAL_COLORS['silver'])
            # Right side
            draw.ellipse([cx + neck_width - 3, peg_y - 2, cx + neck_width + 3, peg_y + 2],
                        fill=METAL_COLORS['silver'])
        
        return img
    
    part.create_image = create_guitar_image
    return part


def create_spiked_arm(name: str = "arm", length: int = 60, width: int = 18) -> Part:
    """Create an arm with spiked metal armor."""
    side = "left" if "left" in name else "right"
    
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,
        color=METAL_COLORS['dark_silver']
    )
    
    def create_arm_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Upper arm (black leather armor with silver studs)
        upper_height = length // 2
        draw.rectangle(
            [2, 2, width-3, upper_height],
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Metal studs on shoulder (more aggressive)
        for i in range(3):
            sx = width // 2 + (i - 1) * 5
            sy = 5
            draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], 
                        fill=METAL_COLORS['silver'],
                        outline=METAL_COLORS['dark_silver'])
        
        # Spikes on shoulder
        spike_x = width // 2
        draw.polygon(
            [(spike_x, -2), (spike_x-5, 10), (spike_x+5, 10)],
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['dark_silver']
        )
        
        # Forearm (skin showing with leather wristband)
        forearm_start = upper_height
        draw.rectangle(
            [4, forearm_start, width-5, length-5],
            fill=METAL_COLORS['skin'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['skin']),
            width=1
        )
        
        # Spiked leather wristband
        wrist_y = length - 15
        draw.rectangle(
            [2, wrist_y, width-3, wrist_y + 10],
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        # Spikes on wristband
        for i in range(3):
            sx = 5 + i * 5
            draw.polygon(
                [(sx, wrist_y - 4), (sx-2, wrist_y), (sx+2, wrist_y)],
                fill=METAL_COLORS['silver']
            )
        
        # Hand
        hand_y = length - 8
        draw.ellipse(
            [width//2 - 6, hand_y - 3, width//2 + 6, hand_y + 8],
            fill=METAL_COLORS['skin'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['skin'])
        )
        
        return img
    
    part.create_image = create_arm_image
    
    part.add_joint(f"elbow_{side}", x=0.5, y=0.5, angle=0, angle_min=-90, angle_max=90)
    part.add_joint(f"wrist_{side}", x=0.5, y=1.0, angle=0, angle_min=-90, angle_max=90)
    
    return part


def create_armored_leg(name: str = "leg", length: int = 70, width: int = 20) -> Part:
    """Create a leg with metal armor and spiked boots."""
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,
        color=METAL_COLORS['black']
    )
    
    def create_leg_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Thigh (black leather pants)
        thigh_height = length // 2
        draw.rectangle(
            [2, 2, width-3, thigh_height],
            fill=METAL_COLORS['black_leather'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['black_leather']),
            width=2
        )
        
        # Metal knee guard with spikes
        knee_y = thigh_height
        draw.rectangle(
            [0, knee_y - 3, width-1, knee_y + 10],
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['dark_silver'],
            width=2
        )
        # Center spike on knee
        draw.polygon(
            [(width//2, knee_y - 6), (width//2-3, knee_y), (width//2+3, knee_y)],
            fill=METAL_COLORS['silver']
        )
        
        # Shin (black leather boot)
        boot_start = knee_y + 8
        draw.rectangle(
            [3, boot_start, width-4, length-10],
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Boot foot with studs
        foot_y = length - 10
        draw.rectangle(
            [2, foot_y, width-3, length-2],
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Metal studs on boot
        for i in range(4):
            sx = 5 + i * 4
            draw.ellipse([sx - 2, foot_y + 2, sx + 2, foot_y + 6],
                        fill=METAL_COLORS['silver'])
        
        return img
    
    part.create_image = create_leg_image
    part.add_joint("knee", x=0.5, y=0.5, angle=0, angle_min=0, angle_max=90)
    
    return part


def create_metal_torso(name: str = "torso", width: int = 55, height: int = 75) -> Part:
    """Create a black leather torso with metal studs and spikes."""
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.5,
        pivot_y=0.5,
        color=METAL_COLORS['black_leather']
    )
    
    def create_torso_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Main body (tapered for female proportions)
        points = [
            (width//3, 2),           # Narrower shoulders
            (width*2//3, 2),
            (width-3, height-3),     # Wider hips
            (2, height-3)
        ]
        draw.polygon(
            points,
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Chest plate detail (smaller, feminine)
        chest_points = [
            (width//3 + 5, 10),
            (width*2//3 - 5, 10),
            (width*2//3 - 5, height//2 - 5),
            (width//2, height//2 + 5),
            (width//3 + 5, height//2 - 5)
        ]
        draw.polygon(
            chest_points,
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Silver studs on chest
        for row in range(2):
            for col in range(3):
                sx = width//2 + (col - 1) * 8
                sy = 18 + row * 10
                draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], 
                            fill=METAL_COLORS['silver'])
        
        # Spiked shoulder pads (more aggressive)
        for i in range(4):
            # Left shoulder
            sx = 4 + i * 5
            sy = 6
            draw.polygon(
                [(sx, sy - 10), (sx-3, sy), (sx+3, sy)],
                fill=METAL_COLORS['silver'],
                outline=METAL_COLORS['dark_silver']
            )
            # Right shoulder
            sx = width - 4 - i * 5
            draw.polygon(
                [(sx, sy - 10), (sx-3, sy), (sx+3, sy)],
                fill=METAL_COLORS['silver'],
                outline=METAL_COLORS['dark_silver']
            )
        
        # Studded belt
        belt_y = height * 3 // 4
        draw.rectangle(
            [3, belt_y, width-4, belt_y + 10],
            fill=METAL_COLORS['black_leather'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Belt studs
        for i in range(5):
            sx = 8 + i * 10
            draw.ellipse([sx - 3, belt_y + 2, sx + 3, belt_y + 8],
                        fill=METAL_COLORS['silver'])
        
        # Belt buckle (spiked)
        draw.rectangle(
            [width//2 - 8, belt_y - 2, width//2 + 8, belt_y + 12],
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['dark_silver'],
            width=2
        )
        # Buckle spikes
        for dx in [-6, 0, 6]:
            draw.polygon(
                [(width//2 + dx, belt_y - 5), (width//2 + dx - 2, belt_y), 
                 (width//2 + dx + 2, belt_y)],
                fill=METAL_COLORS['silver']
            )
        
        return img
    
    part.create_image = create_torso_image
    
    part.add_joint("neck", 0.5, 0.0, angle=0, angle_min=-30, angle_max=30)
    part.add_joint("shoulder_left", 0.1, 0.2, angle=0, angle_min=-180, angle_max=80)
    part.add_joint("shoulder_right", 0.9, 0.2, angle=0, angle_min=-80, angle_max=180)
    part.add_joint("hip_left", 0.3, 1.0, angle=0, angle_min=-90, angle_max=45)
    part.add_joint("hip_right", 0.7, 1.0, angle=0, angle_min=-45, angle_max=90)
    
    return part


def create_metal_head(name: str = "head", size: int = 48) -> Part:
    """Create a metal warrior head with long flowing vibrant red hair."""
    part = Part(
        name=name,
        width=size,
        height=size + 35,  # Extra height for longer hair
        pivot_x=0.5,
        pivot_y=0.65,  # Lower pivot for hair
        color=METAL_COLORS['skin']
    )
    
    def create_head_image():
        img = Image.new('RGBA', (size, size + 35), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        face_size = size
        
        # Long flowing vibrant red hair - BEHIND the head
        hair_color = METAL_COLORS['vibrant_red']
        hair_highlight = (230, 50, 50)  # Lighter red for highlights
        
        # BACK HAIR - flows behind the head, not in front of face
        # This is the hair that goes down the back
        back_hair_points = [
            (0, 10),                      # Top left (behind head)
            (face_size//4, 2),            # Top center-left
            (face_size*3//4, 2),          # Top center-right
            (face_size, 10),               # Top right (behind head)
            (face_size, face_size + 30),   # Bottom right - long flowing back
            (face_size//2, face_size + 35), # Bottom center point
            (0, face_size + 30)            # Bottom left - long flowing back
        ]
        draw.polygon(back_hair_points, fill=hair_color, 
                    outline=(150, 0, 0), width=2)
        
        # Side hair strands - flowing to the sides, NOT in front of face
        # Left side hair
        left_side_hair = [
            (0, 15),
            (-5, face_size//2),
            (0, face_size + 20)
        ]
        draw.polygon(left_side_hair, fill=hair_color, outline=(150, 0, 0), width=1)
        
        # Right side hair
        right_side_hair = [
            (face_size, 15),
            (face_size + 5, face_size//2),
            (face_size, face_size + 20)
        ]
        draw.polygon(right_side_hair, fill=hair_color, outline=(150, 0, 0), width=1)
        
        # Top hair volume - covers top of head
        top_hair_points = [
            (face_size//6, 0),
            (face_size//2, -3),
            (face_size*5//6, 0),
            (face_size*5//6, 15),
            (face_size//2, 12),
            (face_size//6, 15)
        ]
        draw.polygon(top_hair_points, fill=hair_color, outline=(150, 0, 0), width=1)
        
        # Side-swept bangs - frame the face from above, NOT below
        # Left bang - swept to the side
        left_bang = [
            (face_size//6, 5),
            (face_size//3, 3),
            (face_size//3, face_size//4),
            (face_size//6 + 2, face_size//4 + 5)
        ]
        draw.polygon(left_bang, fill=hair_color)
        
        # Right bang - swept to the side
        right_bang = [
            (face_size*2//3, 3),
            (face_size*5//6, 5),
            (face_size*5//6 - 2, face_size//4 + 5),
            (face_size*2//3, face_size//4)
        ]
        draw.polygon(right_bang, fill=hair_color)
        
        # Hair highlight strands on top
        draw.line([(face_size//3, 2), (face_size//3 + 5, 15)], fill=hair_highlight, width=2)
        draw.line([(face_size//2, 0), (face_size//2 + 3, 12)], fill=hair_highlight, width=2)
        draw.line([(face_size*2//3, 2), (face_size*2//3 - 2, 15)], fill=hair_highlight, width=2)
        
        # Face (slightly smaller for female proportions)
        face_margin = 6
        draw.ellipse(
            [face_margin, 8, face_size - face_margin - 1, face_size - 5],
            fill=METAL_COLORS['skin'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['skin']),
            width=2
        )
        
        # Eyes (intense, with dark makeup - metal style)
        eye_y = face_size // 2 - 2
        # Eye shadow/makeup
        draw.ellipse([face_size//3-6, eye_y-5, face_size//3+4, eye_y+5], 
                    fill=(40, 40, 40))
        draw.ellipse([face_size*2//3-4, eye_y-5, face_size*2//3+6, eye_y+5], 
                    fill=(40, 40, 40))
        
        # Eyes themselves (intense)
        draw.ellipse([face_size//3-4, eye_y-3, face_size//3+2, eye_y+3], 
                    fill=(30, 30, 30))
        draw.ellipse([face_size//3-2, eye_y-1, face_size//3, eye_y+1], 
                    fill=METAL_COLORS['vibrant_red'])  # Red eyes
        draw.ellipse([face_size*2//3-2, eye_y-3, face_size*2//3+4, eye_y+3], 
                    fill=(30, 30, 30))
        draw.ellipse([face_size*2//3, eye_y-1, face_size*2//3+2, eye_y+1], 
                    fill=METAL_COLORS['vibrant_red'])
        
        # Eyebrows (intense, arched)
        draw.line([(face_size//3-4, eye_y-6), (face_size//3+2, eye_y-8)],
                 fill=hair_color, width=2)
        draw.line([(face_size*2//3-2, eye_y-8), (face_size*2//3+4, eye_y-6)],
                 fill=hair_color, width=2)
        
        # Mouth (determined/fierce)
        mouth_y = face_size * 2 // 3
        draw.line([(face_size//2-5, mouth_y), (face_size//2+5, mouth_y)],
                 fill=(150, 80, 80), width=2)
        
        return img
    
    part.create_image = create_head_image
    return part
