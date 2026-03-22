"""
Part definitions for the Metal Warrior character.
"""

from PIL import Image, ImageDraw
from typing import Tuple
import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
from core.part import Part


# Metal color palette
METAL_COLORS = {
    'dark_leather': (40, 30, 30),
    'brown_leather': (80, 50, 30),
    'silver': (180, 190, 200),
    'dark_silver': (120, 130, 140),
    'gold': (200, 170, 80),
    'skin': (255, 220, 177),
    'black': (20, 20, 25),
    'red_accent': (180, 30, 30),
}


def create_guitar(
    name: str = "guitar",
    body_width: int = 50,
    body_height: int = 70,
    neck_length: int = 60,
    body_color: Tuple[int, int, int] = (60, 30, 20),
    neck_color: Tuple[int, int, int] = (120, 80, 50),
    accent_color: Tuple[int, int, int] = (200, 170, 80)
) -> Part:
    """Create an electric guitar weapon."""
    total_height = body_height + neck_length
    total_width = body_width + 10
    
    part = Part(
        name=name,
        width=total_width,
        height=total_height,
        pivot_x=0.5,
        pivot_y=0.15,  # Hold at top of neck
        color=body_color
    )
    
    def create_guitar_image():
        img = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx = total_width // 2
        neck_top = 5
        body_top = neck_length
        body_bottom = total_height - 5
        
        # Guitar neck
        neck_width = 12
        draw.rectangle(
            [cx - neck_width//2, neck_top, cx + neck_width//2, body_top + 10],
            fill=neck_color,
            outline=tuple(max(0, c-30) for c in neck_color),
            width=2
        )
        
        # Frets on neck
        for i in range(1, 8):
            fret_y = neck_top + i * (body_top - neck_top) // 8
            draw.line([(cx - neck_width//2, fret_y), (cx + neck_width//2, fret_y)],
                     fill=(200, 200, 200), width=1)
        
        # Guitar body (hourglass shape)
        draw.ellipse(
            [cx - body_width//3, body_top, cx + body_width//3, body_top + body_height//2],
            fill=body_color,
            outline=tuple(max(0, c-40) for c in body_color),
            width=2
        )
        draw.ellipse(
            [cx - body_width//2, body_top + body_height//3, cx + body_width//2, body_bottom],
            fill=body_color,
            outline=tuple(max(0, c-40) for c in body_color),
            width=2
        )
        
        # Bridge
        bridge_y = body_top + body_height * 2 // 3
        draw.rectangle(
            [cx - 12, bridge_y - 3, cx + 12, bridge_y + 3],
            fill=(150, 150, 150),
            outline=(100, 100, 100)
        )
        
        # Pickups
        pickup_y = body_top + body_height // 3
        draw.rectangle(
            [cx - 10, pickup_y - 4, cx + 10, pickup_y + 4],
            fill=(30, 30, 30),
            outline=(100, 100, 100)
        )
        
        # Metal accents/spikes on body
        spike_positions = [
            (cx - body_width//3, body_top + 10),
            (cx + body_width//3, body_top + 15),
            (cx - body_width//2 + 5, body_bottom - 15),
            (cx + body_width//2 - 5, body_bottom - 10),
        ]
        for sx, sy in spike_positions:
            draw.polygon(
                [(sx, sy - 6), (sx - 3, sy + 2), (sx + 3, sy + 2)],
                fill=accent_color,
                outline=tuple(max(0, c-40) for c in accent_color)
            )
        
        # Guitar strings
        for i in range(-2, 3):
            string_x = cx + i * 2
            draw.line(
                [(string_x, neck_top), (string_x, bridge_y)],
                fill=(220, 220, 240),
                width=1
            )
        
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
        
        # Upper arm (armor)
        upper_height = length // 2
        draw.rectangle(
            [2, 2, width-3, upper_height],
            fill=METAL_COLORS['dark_silver'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['dark_silver']),
            width=2
        )
        
        # Spikes on shoulder
        spike_x = width // 2
        draw.polygon(
            [(spike_x, 0), (spike_x-4, 8), (spike_x+4, 8)],
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['dark_silver']
        )
        
        # Forearm (skin showing)
        forearm_start = upper_height
        draw.rectangle(
            [4, forearm_start, width-5, length-5],
            fill=METAL_COLORS['skin'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['skin']),
            width=1
        )
        
        # Leather wristband
        wrist_y = length - 15
        draw.rectangle(
            [3, wrist_y, width-4, wrist_y + 8],
            fill=METAL_COLORS['brown_leather'],
            outline=METAL_COLORS['dark_leather'],
            width=2
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
    """Create a leg with metal armor."""
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
        
        # Thigh (pants)
        thigh_height = length // 2
        draw.rectangle(
            [2, 2, width-3, thigh_height],
            fill=METAL_COLORS['black'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['black']),
            width=2
        )
        
        # Metal knee guard
        knee_y = thigh_height
        draw.rectangle(
            [1, knee_y - 3, width-2, knee_y + 8],
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['dark_silver'],
            width=2
        )
        
        # Shin (boot)
        boot_start = knee_y + 5
        draw.rectangle(
            [3, boot_start, width-4, length-8],
            fill=METAL_COLORS['dark_leather'],
            outline=METAL_COLORS['black'],
            width=2
        )
        
        # Boot foot
        foot_y = length - 8
        draw.rectangle(
            [2, foot_y, width-3, length-2],
            fill=METAL_COLORS['brown_leather'],
            outline=METAL_COLORS['dark_leather'],
            width=2
        )
        
        return img
    
    part.create_image = create_leg_image
    part.add_joint("knee", x=0.5, y=0.5, angle=0, angle_min=0, angle_max=90)
    
    return part


def create_metal_torso(name: str = "torso", width: int = 55, height: int = 75) -> Part:
    """Create a metal-armored torso."""
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.5,
        pivot_y=0.5,
        color=METAL_COLORS['dark_silver']
    )
    
    def create_torso_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Main body (tapered)
        points = [
            (width//4, 2),
            (width*3//4, 2),
            (width-3, height-3),
            (2, height-3)
        ]
        draw.polygon(
            points,
            fill=METAL_COLORS['dark_silver'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        # Chest plate detail
        chest_points = [
            (width//3, 10),
            (width*2//3, 10),
            (width*2//3, height//2),
            (width//2, height//2 + 10),
            (width//3, height//2)
        ]
        draw.polygon(
            chest_points,
            fill=METAL_COLORS['silver'],
            outline=METAL_COLORS['gold'],
            width=2
        )
        
        # Spiked shoulder pads
        for i in range(3):
            sx = 5 + i * 6
            sy = 8
            draw.polygon(
                [(sx, sy - 8), (sx-3, sy), (sx+3, sy)],
                fill=METAL_COLORS['silver'],
                outline=METAL_COLORS['dark_silver']
            )
            sx = width - 5 - i * 6
            draw.polygon(
                [(sx, sy - 8), (sx-3, sy), (sx+3, sy)],
                fill=METAL_COLORS['silver'],
                outline=METAL_COLORS['dark_silver']
            )
        
        # Belt
        belt_y = height * 3 // 4
        draw.rectangle(
            [5, belt_y, width-6, belt_y + 8],
            fill=METAL_COLORS['brown_leather'],
            outline=METAL_COLORS['gold'],
            width=2
        )
        
        # Belt buckle
        draw.rectangle(
            [width//2 - 6, belt_y - 1, width//2 + 6, belt_y + 9],
            fill=METAL_COLORS['gold'],
            outline=METAL_COLORS['silver'],
            width=2
        )
        
        return img
    
    part.create_image = create_torso_image
    
    part.add_joint("neck", 0.5, 0.0, angle=0, angle_min=-30, angle_max=30)
    part.add_joint("shoulder_left", 0.1, 0.2, angle=0, angle_min=-180, angle_max=80)
    part.add_joint("shoulder_right", 0.9, 0.2, angle=0, angle_min=-80, angle_max=180)
    part.add_joint("hip_left", 0.3, 1.0, angle=0, angle_min=-90, angle_max=45)
    part.add_joint("hip_right", 0.7, 1.0, angle=0, angle_min=-45, angle_max=90)
    
    return part


def create_metal_head(name: str = "head", size: int = 42) -> Part:
    """Create a metal warrior head with long hair."""
    part = Part(
        name=name,
        width=size,
        height=size,
        pivot_x=0.5,
        pivot_y=0.8,
        color=METAL_COLORS['skin']
    )
    
    def create_head_image():
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Face
        draw.ellipse(
            [4, 4, size-5, size-5],
            fill=METAL_COLORS['skin'],
            outline=tuple(max(0, c-40) for c in METAL_COLORS['skin']),
            width=2
        )
        
        # Eyes (intense, with dark makeup)
        eye_y = size // 2 - 2
        draw.ellipse([size//3-4, eye_y-3, size//3+2, eye_y+3], fill=(30, 30, 30))
        draw.ellipse([size//3-2, eye_y-1, size//3, eye_y+1], fill=(200, 50, 50))
        draw.ellipse([size*2//3-2, eye_y-3, size*2//3+4, eye_y+3], fill=(30, 30, 30))
        draw.ellipse([size*2//3, eye_y-1, size*2//3+2, eye_y+1], fill=(200, 50, 50))
        
        # Long hair (flowing back)
        hair_color = (40, 30, 25)
        hair_points = [
            (2, size//3), (size//4, 2), (size*3//4, 2),
            (size-2, size//3), (size-2, size*2//3),
            (size//2, size-2), (2, size*2//3)
        ]
        draw.polygon(hair_points, fill=hair_color)
        
        for i in range(3):
            x = size//4 + i * size//4
            draw.line([(x, 4), (x + 5, size-5)], fill=tuple(max(0, c-20) for c in hair_color), width=2)
        
        return img
    
    part.create_image = create_head_image
    return part
