"""
Rig builder for the Metal Warrior character.
"""

import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
from core.rig import Rig
from rigging.parts import (
    create_metal_torso,
    create_metal_head,
    create_metal_back_hair,
    create_spiked_arm,
    create_armored_leg,
    create_guitar,
)


def create_metal_warrior_rig() -> Rig:
    """Create the complete metal warrior rig."""
    
    torso = create_metal_torso("torso")
    
    # Create back hair first (renders behind torso)
    back_hair = create_metal_back_hair("back_hair")
    
    head = create_metal_head("head")
    neck = torso.find_joint("neck")
    if neck:
        neck.child = head
    
    # Attach hair to torso at neck position
    # Hair has pivot at bottom, so it extends UP behind the head
    if neck:
        torso.add_joint(
            "hair_sync",
            x=0.5,  # Same X as neck (center of torso)
            y=0.0,  # At the neck/top of torso - hair pivot (bottom) attaches here
            child=back_hair,
            sync_to=neck,  # Sync to neck joint so hair follows head rotation
            angle_offset=0
        )
    
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
    
    # Create TWO guitar parts for different poses
    
    # Guitar for idle/walk - attached to torso, horizontal playing position
    # Pivot at body (where it rests against torso)
    guitar_torso = create_guitar(
        "guitar_torso",
        body_width=45,
        body_height=60,
        neck_length=50,
        pivot_at_neck=False  # Pivot at body for playing position
    )
    
    # Guitar for attack - attached to wrist, chopping motion
    # Pivot at neck (where hand grips)
    guitar_attack = create_guitar(
        "guitar_attack",
        body_width=45,
        body_height=60,
        neck_length=50,
        pivot_at_neck=True  # Pivot at neck for attack motion
    )
    
    # Attach guitar_torso to a NEW joint on torso (guitar_mount)
    # Position: center of torso, slightly below chest
    torso.add_joint(
        "guitar_mount",
        x=0.5,  # Center of torso
        y=0.6,  # Slightly below chest
        child=guitar_torso,
        angle=0,  # Will be set by pose
        angle_min=-180,
        angle_max=180
    )
    
    # Attach guitar_attack to left wrist (for attack poses)
    # Attack guitar is hidden by default - only shown during attack poses
    guitar_attack.visible = False  # Hide by default, show only for attack poses
    left_wrist = left_arm.find_joint("wrist_left")
    if left_wrist:
        left_wrist.child = guitar_attack
    
    rig = Rig("MetalWarrior", torso, canvas_size=(200, 250))
    rig.root_x = 100
    rig.root_y = 120
    
    return rig