"""
Part definitions for the Imp enemy character.
Heavy Metal Nightmare - Small flying demon enemy
"""

from PIL import Image, ImageDraw
from typing import Tuple
import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
from core.part import Part


# Imp color palette
IMP_COLORS = {
    'body_red': (200, 40, 40),          # Main red body
    'body_dark': (140, 25, 25),         # Darker red for shading
    'body_light': (230, 60, 60),        # Lighter red for highlights
    'horn_black': (30, 30, 35),         # Black horns
    'eye_yellow': (255, 220, 60),       # Yellow eyes
    'pupil_black': (20, 20, 25),          # Black pupils
    'wing_purple': (120, 40, 120),      # Purple/magenta wings
    'wing_dark': (80, 25, 80),          # Darker wing membrane
    'wing_light': (160, 60, 160),       # Lighter wing highlights
    'claw_gray': (100, 100, 110),       # Gray claws
    'tail_tip': (20, 20, 25),           # Black tail tip
    'teeth_white': (240, 240, 240),     # White teeth
    'mouth_dark': (80, 20, 20),         # Dark mouth interior
}


def create_imp_body(name: str = "body", width: int = 30, height: int = 28) -> Part:
    """Create a round red imp torso."""
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.5,
        pivot_y=0.5,
        color=IMP_COLORS['body_red'],
        z_index=0
    )
    
    def create_body_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx, cy = width // 2, height // 2
        
        # Main round body
        body_radius = min(width, height) // 2 - 2
        draw.ellipse(
            [cx - body_radius, cy - body_radius, 
             cx + body_radius, cy + body_radius],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=2
        )
        
        # Chest highlight (lighter red)
        highlight_radius = body_radius // 2
        draw.ellipse(
            [cx - highlight_radius//2, cy - highlight_radius//2 - 2,
             cx + highlight_radius//2, cy + highlight_radius//2 - 2],
            fill=IMP_COLORS['body_light']
        )
        
        # Small belly detail
        draw.ellipse(
            [cx - 4, cy + 4, cx + 4, cy + 10],
            fill=IMP_COLORS['body_dark']
        )
        
        return img
    
    part.create_image = create_body_image
    return part


def create_imp_head(name: str = "head", size: int = 24) -> Part:
    """Create imp head with horns, yellow eyes, and grin."""
    # Extra height for horns
    total_height = size + 12
    total_width = size + 8
    
    part = Part(
        name=name,
        width=total_width,
        height=total_height,
        pivot_x=0.5,
        pivot_y=0.75,  # Lower pivot to connect to body
        color=IMP_COLORS['body_red'],
        z_index=1
    )
    
    def create_head_image():
        img = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx = total_width // 2
        face_top = 12  # Space for horns
        face_size = size
        
        # Horns (black, curved)
        # Left horn
        horn_left_points = [
            (cx - 6, face_top + 2),
            (cx - 10, face_top - 8),
            (cx - 4, face_top - 6),
            (cx - 2, face_top + 2)
        ]
        draw.polygon(horn_left_points, fill=IMP_COLORS['horn_black'], 
                    outline=tuple(c - 20 for c in IMP_COLORS['horn_black']))
        # Right horn
        horn_right_points = [
            (cx + 6, face_top + 2),
            (cx + 10, face_top - 8),
            (cx + 4, face_top - 6),
            (cx + 2, face_top + 2)
        ]
        draw.polygon(horn_right_points, fill=IMP_COLORS['horn_black'],
                    outline=tuple(c - 20 for c in IMP_COLORS['horn_black']))
        
        # Face (round red)
        face_margin = 2
        draw.ellipse(
            [face_margin, face_top, total_width - face_margin, face_top + face_size - 2],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=2
        )
        
        # Eyes (yellow with black pupils)
        eye_y = face_top + face_size // 2 - 2
        eye_size = 5
        pupil_size = 2
        
        # Left eye
        draw.ellipse(
            [cx - 6 - eye_size//2, eye_y - eye_size//2,
             cx - 6 + eye_size//2, eye_y + eye_size//2],
            fill=IMP_COLORS['eye_yellow'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        draw.ellipse(
            [cx - 6 - pupil_size//2, eye_y - pupil_size//2,
             cx - 6 + pupil_size//2, eye_y + pupil_size//2],
            fill=IMP_COLORS['pupil_black']
        )
        
        # Right eye
        draw.ellipse(
            [cx + 6 - eye_size//2, eye_y - eye_size//2,
             cx + 6 + eye_size//2, eye_y + eye_size//2],
            fill=IMP_COLORS['eye_yellow'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        draw.ellipse(
            [cx + 6 - pupil_size//2, eye_y - pupil_size//2,
             cx + 6 + pupil_size//2, eye_y + pupil_size//2],
            fill=IMP_COLORS['pupil_black']
        )
        
        # Eyebrows (angry expression)
        draw.line([(cx - 9, eye_y - 5), (cx - 3, eye_y - 3)], 
                 fill=IMP_COLORS['horn_black'], width=2)
        draw.line([(cx + 3, eye_y - 3), (cx + 9, eye_y - 5)], 
                 fill=IMP_COLORS['horn_black'], width=2)
        
        # Grinning mouth with teeth
        mouth_y = face_top + face_size * 2 // 3
        # Mouth background
        draw.arc(
            [cx - 7, mouth_y - 5, cx + 7, mouth_y + 5],
            start=0, end=180,
            fill=IMP_COLORS['mouth_dark'],
            width=3
        )
        # Teeth (white points)
        for i in range(-2, 3):
            tx = cx + i * 3
            tooth_y = mouth_y + 1 if i % 2 == 0 else mouth_y + 3
            draw.polygon(
                [(tx - 1, tooth_y - 2), (tx + 1, tooth_y - 2), (tx, tooth_y + 2)],
                fill=IMP_COLORS['teeth_white']
            )
        
        return img
    
    part.create_image = create_head_image
    return part


def create_imp_wing(name: str = "wing", width: int = 32, height: int = 28) -> Part:
    """Create a bat-like purple wing."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.15 if is_left else 0.85,  # Pivot near body attachment (edge of image)
        pivot_y=0.85,
        color=IMP_COLORS['wing_purple'],
        z_index=-1
    )
    
    def create_wing_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Wing attachment point - near the edge where it connects to body
        attach_x = 4 if is_left else width - 4
        attach_y = height - 4
        
        # Wing shape - bat-like, NARROWER for folded/back appearance
        # Wings are positioned behind body, so they should be compact and not stick out
        if is_left:
            # Left wing: attached at left edge, extends slightly inward
            wing_points = [
                (attach_x, attach_y),              # Body attachment (left edge)
                (attach_x + 3, attach_y - 4),      # Inner curve (closer)
                (width//2 + 2, attach_y - height + 10),  # Top tip (lower/closer)
                (width - 6, attach_y - height//3), # Outer point (closer to body)
                (width - 8, attach_y - 2),         # Bottom edge
                (attach_x + 2, attach_y - 2)       # Back near attachment
            ]
            
            # Wing membrane veins (shorter for compact wings)
            membrane_lines = [
                ((attach_x, attach_y), (width//2 + 2, attach_y - height + 10)),
                ((attach_x + 3, attach_y - 4), (width - 6, attach_y - height//3)),
                ((width - 6, attach_y - height//3), (width - 8, attach_y - 2)),
            ]
        else:
            # Right wing: attached at right edge, extends slightly inward
            wing_points = [
                (attach_x, attach_y),              # Body attachment (right edge)
                (attach_x - 3, attach_y - 4),      # Inner curve (closer)
                (width//2 - 2, attach_y - height + 10),  # Top tip (lower/closer)
                (6, attach_y - height//3),        # Outer point (closer to body)
                (8, attach_y - 2),                 # Bottom edge
                (attach_x - 2, attach_y - 2)       # Back near attachment
            ]
            
            # Wing membrane veins (shorter for compact wings)
            membrane_lines = [
                ((attach_x, attach_y), (width//2 - 2, attach_y - height + 10)),
                ((attach_x - 3, attach_y - 4), (6, attach_y - height//3)),
                ((6, attach_y - height//3), (8, attach_y - 2)),
            ]
        
        # Draw wing membrane
        draw.polygon(wing_points, fill=IMP_COLORS['wing_purple'],
                    outline=IMP_COLORS['wing_dark'], width=2)
        
        # Draw wing veins
        for start, end in membrane_lines:
            draw.line([start, end], fill=IMP_COLORS['wing_dark'], width=1)
        
        # Wing highlight (adjusted for narrower wings)
        if is_left:
            highlight_points = [
                (attach_x + 3, attach_y - 4),
                (width//2, attach_y - height + 12),
                (width - 10, attach_y - height//3 + 2),
            ]
        else:
            highlight_points = [
                (attach_x - 3, attach_y - 4),
                (width//2, attach_y - height + 12),
                (10, attach_y - height//3 + 2),
            ]
        for i in range(len(highlight_points) - 1):
            draw.line([highlight_points[i], highlight_points[i+1]], 
                     fill=IMP_COLORS['wing_light'], width=2)
        
        return img
    
    part.create_image = create_wing_image
    return part


def create_imp_arm(name: str = "arm", length: int = 14, width: int = 8) -> Part:
    """Create a small red arm with claw."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,  # Pivot at shoulder
        color=IMP_COLORS['body_red'],
        z_index=0
    )
    
    def create_arm_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Upper arm (red)
        upper_length = length * 2 // 3
        draw.rectangle(
            [1, 1, width - 2, upper_length],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        # Forearm
        draw.rectangle(
            [2, upper_length, width - 3, length - 4],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        # Claw hand
        claw_y = length - 3
        claw_x = width // 2
        
        # Three claws
        claw_offsets = [-2, 0, 2]
        for dx in claw_offsets:
            points = [
                (claw_x + dx - 1, claw_y - 3),
                (claw_x + dx, claw_y + 2),
                (claw_x + dx + 1, claw_y - 3)
            ]
            draw.polygon(points, fill=IMP_COLORS['claw_gray'],
                        outline=IMP_COLORS['horn_black'])
        
        return img
    
    part.create_image = create_arm_image
    part.add_joint(f"elbow_{'left' if is_left else 'right'}", 
                   x=0.5, y=0.6, angle=0, angle_min=-60, angle_max=60)
    
    return part


def create_imp_leg(name: str = "leg", length: int = 16, width: int = 6) -> Part:
    """Create a thin leg with small foot."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,  # Pivot at hip
        color=IMP_COLORS['body_red'],
        z_index=0
    )
    
    def create_leg_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Thin leg
        leg_width = 3
        draw.rectangle(
            [(width - leg_width) // 2, 1, (width + leg_width) // 2, length - 4],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        # Small foot
        foot_y = length - 3
        draw.ellipse(
            [1, foot_y - 2, width - 2, foot_y + 3],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        return img
    
    part.create_image = create_leg_image
    part.add_joint(f"knee_{'left' if is_left else 'right'}",
                   x=0.5, y=0.5, angle=0, angle_min=-30, angle_max=30)
    
    return part


def create_imp_tail(name: str = "tail", width: int = 30, height: int = 36) -> Part:
    """Create a whip-like devil tail with constant width and black spade tip.
    
    Thin tail (2-3px) with a smooth S-curve, same width throughout.
    Black spade tip at the end. Renders BEHIND the body using z_index=-1.
    """
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.15,   # Pivot near left edge (tail attachment)
        pivot_y=0.9,    # Near bottom where it attaches to body
        z_index=-1      # Renders BEHIND body
    )
    
    def create_tail_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Colors
        tail_red = IMP_COLORS['body_red']      # (200, 40, 40)
        tail_dark = IMP_COLORS['body_dark']    # Darker red
        
        # S-curve points - constant width tail
        # Starting from attachment point (bottom left)
        # Curve: starts down/right, curves up, then curls back
        tail_thickness = 2  # CONSTANT width throughout!
        
        # S-curve path points (x, y)
        curve_points = [
            (3, 33),    # Attachment to body
            (5, 30),
            (8, 26),
            (12, 22),   # Middle of first curve
            (16, 20),
            (20, 19),
            (22, 21),   # Start of S curve back
            (21, 25),
            (18, 28),   # Tip position
        ]
        
        # Draw the tail as a smooth line with constant thickness
        for i in range(len(curve_points) - 1):
            x1, y1 = curve_points[i]
            x2, y2 = curve_points[i + 1]
            draw.line([(x1, y1), (x2, y2)], fill=tail_red, width=tail_thickness)
            # Dark outline
            draw.line([(x1, y1), (x2, y2)], fill=tail_dark, width=1)
        
        # Fill in the line to make it solid (circles at each point)
        for x, y in curve_points:
            draw.ellipse([x-1, y-1, x+1, y+1], fill=tail_red, outline=tail_dark, width=1)
        
        # BLACK SPADE TIP at the end
        tip_x, tip_y = curve_points[-1]
        
        # Small spade/arrow shape pointing up and left
        spade_points = [
            (tip_x - 2, tip_y + 1),      # Left base
            (tip_x, tip_y - 4),          # Sharp top point  
            (tip_x + 2, tip_y + 1),      # Right base
            (tip_x, tip_y + 2),          # Bottom indent
        ]
        
        draw.polygon(spade_points, fill=IMP_COLORS['tail_tip'], outline=(10, 10, 10))
        
        return img
    
    part.create_image = create_tail_image
    return part
