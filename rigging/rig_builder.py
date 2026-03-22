"""
Rig builder for the Metal Warrior character.
"""

import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
from core.rig import Rig
from rigging.parts import (
    create_metal_torso,
    create_metal_head,
    create_spiked_arm,
    create_armored_leg,
    create_guitar,
)


def create_metal_warrior_rig() -> Rig:
    """Create the complete metal warrior rig."""
    
    torso = create_metal_torso("torso")
    
    head = create_metal_head("head")
    neck = torso.find_joint("neck")
    if neck:
        neck.child = head
    
    left_arm = create_spiked_arm("left_arm", length=60)
    right_arm = create_spiked_arm("right_arm", length=60)
    
    left_shoulder = torso.find_joint("shoulder_left")
    right_shoulder = torso.find_joint("shoulder_right")
    if left_shoulder:
        left_shoulder.child = left_arm
    if right_shoulder:
        right_shoulder.child = right_arm
    
    left_leg = create_armored_leg("left_leg", length=70)
    right_leg = create_armored_leg("right_leg", length=70)
    
    left_hip = torso.find_joint("hip_left")
    right_hip = torso.find_joint("hip_right")
    if left_hip:
        left_hip.child = left_leg
    if right_hip:
        right_hip.child = right_leg
    
    guitar = create_guitar("guitar", body_width=45, body_height=60, neck_length=50)
    # Attach guitar to LEFT WRIST so it moves with the arm
    # This allows for chopping attacks where guitar follows hand motion
    left_wrist = left_arm.find_joint("wrist_left")
    if left_wrist:
        left_wrist.child = guitar
    
    rig = Rig("MetalWarrior", torso, canvas_size=(200, 250))
    rig.root_x = 100
    rig.root_y = 120
    
    return rig
