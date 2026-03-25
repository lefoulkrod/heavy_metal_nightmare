"""
Rig builder for the Imp enemy character.
Heavy Metal Nightmare - Small flying demon enemy
"""

import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
from core.rig import Rig
from rigging.imp.parts import (
    create_imp_body,
    create_imp_head,
    create_imp_wing,
    create_imp_arm,
    create_imp_leg,
    create_imp_tail,
)


def create_imp_rig() -> Rig:
    """
    Create the complete imp rig.
    
    Hierarchy:
    - body (root)
      - head (attached to body via neck joint)
      - left_wing (attached to body back)
      - right_wing (attached to body back)
      - left_arm (attached via shoulder)
      - right_arm (attached via shoulder)
      - left_leg (attached via hip)
      - right_leg (attached via hip)
      - tail (attached to lower body)
    
    Canvas: 100x100 (smaller than player's 200x250)
    """
    
    # Create body as root
    body = create_imp_body("body", width=30, height=28)
    
    # Add attachment joints to body
    # Neck joint for head
    body.add_joint(
        "neck",
        x=0.5, y=0.15,  # Top center of body
        angle=0,
        angle_min=-30,
        angle_max=30
    )
    
    # Shoulder joints for arms
    body.add_joint(
        "shoulder_left",
        x=0.15, y=0.35,  # Left side, upper body
        angle=0,
        angle_min=-90,
        angle_max=60
    )
    body.add_joint(
        "shoulder_right",
        x=0.85, y=0.35,  # Right side, upper body
        angle=0,
        angle_min=-60,
        angle_max=90
    )
    
    # Wing joints (back of body) - positioned behind body, more centered
    body.add_joint(
        "wing_left",
        x=0.35, y=0.45,  # More centered, slightly lower (behind body)
        angle=0,
        angle_min=-60,
        angle_max=60
    )
    body.add_joint(
        "wing_right",
        x=0.65, y=0.45,  # More centered, slightly lower (behind body)
        angle=0,
        angle_min=-60,
        angle_max=60
    )
    
    # Hip joints for legs
    body.add_joint(
        "hip_left",
        x=0.35, y=0.9,  # Lower left
        angle=0,
        angle_min=-45,
        angle_max=45
    )
    body.add_joint(
        "hip_right",
        x=0.65, y=0.9,  # Lower right
        angle=0,
        angle_min=-45,
        angle_max=45
    )
    
    # Tail joint (lower back/bottom center of body, fixed at 45 degrees up-right)
    body.add_joint(
        "tail_base",
        x=0.5, y=0.88,   # Bottom center of body (lower back)
        angle=-45,       # Fixed at 45 degrees pointing up-right
        angle_min=-45,   # Locked - cannot move
        angle_max=-45    # Locked - cannot move
    )
    
    # Create parts
    head = create_imp_head("head", size=24)
    left_wing = create_imp_wing("left_wing", width=24, height=28)  # Narrower wings
    right_wing = create_imp_wing("right_wing", width=24, height=28)  # Narrower wings
    left_arm = create_imp_arm("left_arm", length=14, width=8)
    right_arm = create_imp_arm("right_arm", length=14, width=8)
    left_leg = create_imp_leg("left_leg", length=16, width=6)
    right_leg = create_imp_leg("right_leg", length=16, width=6)
    tail = create_imp_tail("tail", width=24, height=40)
    
    # Attach parts to joints
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
    
    # Create the rig with smaller canvas (100x100 vs player's 200x250)
    rig = Rig("Imp", body, canvas_size=(100, 100))
    rig.root_x = 50   # Center horizontally
    rig.root_y = 55   # Slightly above center to account for hovering
    
    return rig
