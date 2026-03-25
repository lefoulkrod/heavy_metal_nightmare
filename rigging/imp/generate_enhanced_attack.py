#!/usr/bin/env python3
"""
Generate enhanced Imp attack sprite with MORE prominent tail.

The tail is made:
- Longer (extends further out)
- Thicker (more visible width)
- Brighter (vibrant red color)
- More clearly positioned from lower back
"""

import sys
import os

# Add paths
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
sys.path.insert(0, '/home/computron/repos/heavy_metal_nightmare')

from PIL import Image, ImageDraw
from core.part import Part
from core.rig import Rig

# Imp color palette
IMP_COLORS = {
    'body_red': (200, 40, 40),
    'body_dark': (140, 25, 25),
    'body_light': (230, 60, 60),
    'horn_black': (30, 30, 35),
    'eye_yellow': (255, 220, 60),
    'pupil_black': (20, 20, 25),
    'wing_purple': (120, 40, 120),
    'wing_dark': (80, 25, 80),
    'wing_light': (160, 60, 160),
    'claw_gray': (100, 100, 110),
    'tail_tip': (20, 20, 25),
    'teeth_white': (240, 240, 240),
    'mouth_dark': (80, 20, 20),
}


def create_prominent_tail(name="tail", length=48, width=24):
    """
    Create a MORE prominent devil tail that is:
    - LONGER (extends further out)
    - THICKER (wider for visibility)
    - BRIGHTER (vibrant red color)
    """
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.9,
        color=IMP_COLORS['body_red'],
        z_index=-1  # Renders BEHIND body
    )
    
    def create_tail_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # SUPER bright red for maximum visibility
        bright_red = (255, 60, 60)
        brighter_highlight = (255, 140, 140)
        
        # Base at bottom center (attachment to body)
        base_x = width // 2
        base_y = length - 4
        
        # More segments for longer, more prominent tail
        # Extends UP and to the RIGHT from lower back
        segments = [
            (base_x, base_y - 2, 18),       # Base - THICK and prominent
            (base_x + 1, base_y - 6, 17),   # Starting curve
            (base_x + 3, base_y - 10, 16),  # Continuing up-right
            (base_x + 5, base_y - 14, 15),  # Mid section
            (base_x + 6, base_y - 18, 14),  # Continuing
            (base_x + 7, base_y - 22, 13),  # Still thick
            (base_x + 8, base_y - 26, 12),  # Maintaining width
            (base_x + 9, base_y - 30, 11),  # Continuing up
            (base_x + 9, base_y - 34, 10),  # Still visible
            (base_x + 9, base_y - 38, 8),   # Tapering slightly
            (base_x + 8, base_y - 42, 6),   # Near tip
            (base_x + 7, base_y - 45, 4),   # Thinner at end
        ]
        
        # Draw each tail segment - THICK and BRIGHT
        for x, y, w in segments:
            draw.ellipse(
                [x - w//2, y - 5, x + w//2, y + 5],
                fill=bright_red,
                outline=IMP_COLORS['body_dark'],
                width=3  # THICKER outline
            )
        
        # Fill gaps with extra thick connecting polygons
        for i in range(len(segments) - 1):
            x1, y1, w1 = segments[i]
            x2, y2, w2 = segments[i + 1]
            
            points = [
                (x1 - w1//2, y1 + 4),
                (x1 + w1//2, y1 + 4),
                (x2 + w2//2, y2 - 4),
                (x2 - w2//2, y2 - 4),
            ]
            draw.polygon(points, fill=bright_red)
            draw.line(points + [points[0]], fill=IMP_COLORS['body_dark'], width=3)
        
        # Multiple bright highlight stripes for extra visibility
        for i in range(len(segments) - 1):
            x1, y1, w1 = segments[i]
            x2, y2, w2 = segments[i + 1]
            # Strong highlight down the center
            draw.line([(x1 - 3, y1 - 2), (x2 - 3, y2 - 2)], 
                     fill=brighter_highlight, width=3)
            draw.line([(x1 + 3, y1 - 2), (x2 + 3, y2 - 2)], 
                     fill=brighter_highlight, width=2)
        
        # Large, prominent black pointed tip
        tip_x = segments[-1][0]
        tip_y = segments[-1][1] - 6
        
        tip_points = [
            (tip_x - 2, tip_y + 3),
            (tip_x + 2, tip_y + 3),
            (tip_x + 4, tip_y),
            (tip_x, tip_y - 7),         # Sharp point
            (tip_x - 3, tip_y),
        ]
        draw.polygon(tip_points, fill=IMP_COLORS['tail_tip'],
                    outline=IMP_COLORS['horn_black'], width=3)
        
        return img
    
    part.create_image = create_tail_image
    return part


def create_imp_body(name="body", width=30, height=28):
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
        
        body_radius = min(width, height) // 2 - 2
        draw.ellipse(
            [cx - body_radius, cy - body_radius, 
             cx + body_radius, cy + body_radius],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=2
        )
        
        highlight_radius = body_radius // 2
        draw.ellipse(
            [cx - highlight_radius//2, cy - highlight_radius//2 - 2,
             cx + highlight_radius//2, cy + highlight_radius//2 - 2],
            fill=IMP_COLORS['body_light']
        )
        
        draw.ellipse(
            [cx - 4, cy + 4, cx + 4, cy + 10],
            fill=IMP_COLORS['body_dark']
        )
        
        return img
    
    part.create_image = create_body_image
    return part


def create_imp_head(name="head", size=24):
    """Create imp head with horns, yellow eyes, and grin."""
    total_height = size + 12
    total_width = size + 8
    
    part = Part(
        name=name,
        width=total_width,
        height=total_height,
        pivot_x=0.5,
        pivot_y=0.75,
        color=IMP_COLORS['body_red'],
        z_index=1
    )
    
    def create_head_image():
        img = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx = total_width // 2
        face_top = 12
        face_size = size
        
        # Horns
        horn_left_points = [
            (cx - 6, face_top + 2),
            (cx - 10, face_top - 8),
            (cx - 4, face_top - 6),
            (cx - 2, face_top + 2)
        ]
        draw.polygon(horn_left_points, fill=IMP_COLORS['horn_black'])
        
        horn_right_points = [
            (cx + 6, face_top + 2),
            (cx + 10, face_top - 8),
            (cx + 4, face_top - 6),
            (cx + 2, face_top + 2)
        ]
        draw.polygon(horn_right_points, fill=IMP_COLORS['horn_black'])
        
        # Face
        face_margin = 2
        draw.ellipse(
            [face_margin, face_top, total_width - face_margin, face_top + face_size - 2],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=2
        )
        
        # Eyes
        eye_y = face_top + face_size // 2 - 2
        eye_size = 5
        pupil_size = 2
        
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
        
        # Eyebrows
        draw.line([(cx - 9, eye_y - 5), (cx - 3, eye_y - 3)], 
                 fill=IMP_COLORS['horn_black'], width=2)
        draw.line([(cx + 3, eye_y - 3), (cx + 9, eye_y - 5)], 
                 fill=IMP_COLORS['horn_black'], width=2)
        
        # Mouth
        mouth_y = face_top + face_size * 2 // 3
        draw.arc(
            [cx - 7, mouth_y - 5, cx + 7, mouth_y + 5],
            start=0, end=180,
            fill=IMP_COLORS['mouth_dark'],
            width=3
        )
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


def create_imp_wing(name="wing", width=32, height=28):
    """Create a bat-like purple wing."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=height,
        pivot_x=0.15 if is_left else 0.85,
        pivot_y=0.85,
        color=IMP_COLORS['wing_purple'],
        z_index=-1
    )
    
    def create_wing_image():
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        attach_x = 4 if is_left else width - 4
        attach_y = height - 4
        
        if is_left:
            wing_points = [
                (attach_x, attach_y),
                (attach_x + 3, attach_y - 4),
                (width//2 + 2, attach_y - height + 10),
                (width - 6, attach_y - height//3),
                (width - 8, attach_y - 2),
                (attach_x + 2, attach_y - 2)
            ]
        else:
            wing_points = [
                (attach_x, attach_y),
                (attach_x - 3, attach_y - 4),
                (width//2 - 2, attach_y - height + 10),
                (6, attach_y - height//3),
                (8, attach_y - 2),
                (attach_x - 2, attach_y - 2)
            ]
        
        draw.polygon(wing_points, fill=IMP_COLORS['wing_purple'],
                    outline=IMP_COLORS['wing_dark'], width=2)
        
        return img
    
    part.create_image = create_wing_image
    return part


def create_imp_arm(name="arm", length=14, width=8):
    """Create a small red arm with claw."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,
        color=IMP_COLORS['body_red'],
        z_index=0
    )
    
    def create_arm_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        upper_length = length * 2 // 3
        draw.rectangle(
            [1, 1, width - 2, upper_length],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        draw.rectangle(
            [2, upper_length, width - 3, length - 4],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        claw_y = length - 3
        claw_x = width // 2
        
        claw_offsets = [-2, 0, 2]
        for dx in claw_offsets:
            points = [
                (claw_x + dx - 1, claw_y - 3),
                (claw_x + dx, claw_y + 2),
                (claw_x + dx + 1, claw_y - 3)
            ]
            draw.polygon(points, fill=IMP_COLORS['claw_gray'])
        
        return img
    
    part.create_image = create_arm_image
    return part


def create_imp_leg(name="leg", length=16, width=6):
    """Create a thin leg with small foot."""
    is_left = "left" in name.lower()
    
    part = Part(
        name=name,
        width=width,
        height=length,
        pivot_x=0.5,
        pivot_y=0.0,
        color=IMP_COLORS['body_red'],
        z_index=0
    )
    
    def create_leg_image():
        img = Image.new('RGBA', (width, length), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        leg_width = 3
        draw.rectangle(
            [(width - leg_width) // 2, 1, (width + leg_width) // 2, length - 4],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        foot_y = length - 3
        draw.ellipse(
            [1, foot_y - 2, width - 2, foot_y + 3],
            fill=IMP_COLORS['body_red'],
            outline=IMP_COLORS['body_dark'],
            width=1
        )
        
        return img
    
    part.create_image = create_leg_image
    return part


def create_enhanced_imp_rig():
    """Create imp rig with ENHANCED prominent tail."""
    
    # Create body as root
    body = create_imp_body("body", width=30, height=28)
    
    # Add joints
    body.add_joint("neck", x=0.5, y=0.15, angle=0, angle_min=-30, angle_max=30)
    body.add_joint("shoulder_left", x=0.15, y=0.35, angle=0, angle_min=-90, angle_max=60)
    body.add_joint("shoulder_right", x=0.85, y=0.35, angle=0, angle_min=-60, angle_max=90)
    body.add_joint("wing_left", x=0.35, y=0.45, angle=0, angle_min=-60, angle_max=60)
    body.add_joint("wing_right", x=0.65, y=0.45, angle=0, angle_min=-60, angle_max=60)
    body.add_joint("hip_left", x=0.35, y=0.9, angle=0, angle_min=-45, angle_max=45)
    body.add_joint("hip_right", x=0.65, y=0.9, angle=0, angle_min=-45, angle_max=45)
    
    # Tail joint - positioned at lower back, extends up and out
    body.add_joint(
        "tail_base",
        x=0.5, y=0.88,
        angle=-100,
        angle_min=-140,
        angle_max=-60
    )
    
    # Create parts
    head = create_imp_head("head", size=24)
    left_wing = create_imp_wing("left_wing", width=24, height=28)
    right_wing = create_imp_wing("right_wing", width=24, height=28)
    left_arm = create_imp_arm("left_arm", length=14, width=8)
    right_arm = create_imp_arm("right_arm", length=14, width=8)
    left_leg = create_imp_leg("left_leg", length=16, width=6)
    right_leg = create_imp_leg("right_leg", length=16, width=6)
    
    # ENHANCED PROMINENT TAIL - longer and thicker
    tail = create_prominent_tail("tail", length=48, width=24)
    
    # Attach parts
    neck = body.find_joint("neck")
    if neck:
        neck.child = head
    
    shoulder_left = body.find_joint("shoulder_left")
    if shoulder_left:
        shoulder_left.child = left_arm
    
    shoulder_right = body.find_joint("shoulder_right")
    if shoulder_right:
        shoulder_right.child = right_arm
    
    wing_left = body.find_joint("wing_left")
    if wing_left:
        wing_left.child = left_wing
    
    wing_right = body.find_joint("wing_right")
    if wing_right:
        wing_right.child = right_wing
    
    hip_left = body.find_joint("hip_left")
    if hip_left:
        hip_left.child = left_leg
    
    hip_right = body.find_joint("hip_right")
    if hip_right:
        hip_right.child = right_leg
    
    tail_base = body.find_joint("tail_base")
    if tail_base:
        tail_base.child = tail
    
    # Create rig with larger canvas to accommodate longer tail
    rig = Rig("Imp", body, canvas_size=(120, 120))
    rig.root_x = 60
    rig.root_y = 65
    
    return rig


def generate_enhanced_attack_sprite(output_path):
    """Generate attack sprite with prominent tail."""
    
    rig = create_enhanced_imp_rig()
    
    # Attack pose angles - WITH MORE TAIL EXTENSION
    pose_angles = {
        "neck": 25,
        "wing_left": -75,
        "wing_right": 75,
        "shoulder_right": -85,
        "elbow_right": -45,
        "shoulder_left": -75,
        "elbow_left": -40,
        "hip_left": -35,
        "knee_left": -20,
        "hip_right": 40,
        "knee_right": 25,
        "tail_base": -130,  # MORE extreme angle for prominent visibility
    }
    
    # Apply pose
    rig.apply_pose(pose_angles)
    
    # Forward lean offset
    rig.root_x = 60 + 15
    rig.root_y = 65 + 5
    
    # Render
    img = rig.render()
    
    # Save
    img.save(output_path)
    print(f"Generated enhanced attack sprite: {output_path}")
    
    return output_path


if __name__ == "__main__":
    output_path = "/home/computron/repos/heavy_metal_nightmare/sprites_imp/enemy_imp_attack.png"
    generate_enhanced_attack_sprite(output_path)
