"""
Animation poses for the Imp enemy character.

The Imp is a small flying demon with bat-like wings.
Its poses emphasize hovering, wing flapping, and sudden attacks.
"""

import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
from core.pose import Pose


def get_imp_idle_pose():
    """
    Idle pose - Wings folded, hovering gently.
    
    Arms relaxed, legs dangling, tail curled.
    Imp is floating in place with minimal movement.
    """
    return Pose(
        name="imp_idle",
        angles={
            # Head neutral
            "neck": 0,
            
            # Wings folded down
            "wing_left": 15,      # Slight downward angle
            "wing_right": -15,    # Mirror
            
            # Arms relaxed
            "shoulder_left": 20,
            "elbow_left": 10,
            "shoulder_right": -20,
            "elbow_right": -10,
            
            # Legs dangling down
            "hip_left": 10,
            "knee_left": 5,
            "hip_right": -10,
            "knee_right": -5,
            
        },
        root_offset=(0, 0)
    )


def get_imp_float1_pose():
    """
    Float pose 1 - Wings up (flap cycle peak).
    
    Wings raised high as if catching air.
    Body slightly elevated.
    """
    return Pose(
        name="imp_float1",
        angles={
            # Head looking slightly up
            "neck": -5,
            
            # Wings raised up
            "wing_left": -35,     # Raised up
            "wing_right": 35,     # Mirror
            
            # Arms slightly raised with wings
            "shoulder_left": 10,
            "elbow_left": -15,
            "shoulder_right": -10,
            "elbow_right": 15,
            
            # Legs tucked slightly
            "hip_left": -5,
            "knee_left": 10,
            "hip_right": 5,
            "knee_right": -10,
            
        },
        root_offset=(0, -3)  # Slightly higher
    )


def get_imp_float2_pose():
    """
    Float pose 2 - Wings down (flap cycle trough).
    
    Wings pushed down for lift.
    Body slightly lowered.
    """
    return Pose(
        name="imp_float2",
        angles={
            # Head looking slightly down
            "neck": 5,
            
            # Wings pushed down
            "wing_left": 40,      # Pushed down
            "wing_right": -40,    # Mirror
            
            # Arms down with wings
            "shoulder_left": 30,
            "elbow_left": 5,
            "shoulder_right": -30,
            "elbow_right": -5,
            
            # Legs extended down
            "hip_left": 15,
            "knee_left": 5,
            "hip_right": -15,
            "knee_right": -5,
            
        },
        root_offset=(0, 2)  # Slightly lower
    )


def get_imp_attack_pose():
    """
    Attack pose - Forward lunge, claws extended.
    
    Imp lunges forward to slash with claws.
    Wings spread wide for stability.
    Aggressive expression.
    """
    return Pose(
        name="imp_attack",
        angles={
            # Head tilted down looking at target aggressively
            "neck": 25,
            
            # Wings flared out aggressively
            "wing_left": -75,     # Aggressively flared back
            "wing_right": 75,     # Aggressively flared back
            
            # Both arms reaching forward to attack
            "shoulder_right": -85,   # Far forward reaching
            "elbow_right": -45,      # Claws curved to strike
            "shoulder_left": -75,    # Also forward for dual claw attack
            "elbow_left": -40,
            
            # Legs extended back with extreme angles
            "hip_left": -35,
            "knee_left": -20,
            "hip_right": 40,
            "knee_right": 25,
            
        },
        root_offset=(18, 5)  # Strong forward lean
    )


# Pose library for easy access
IMP_POSES = {
    "idle": get_imp_idle_pose,
    "float1": get_imp_float1_pose,
    "float2": get_imp_float2_pose,
    "attack": get_imp_attack_pose,
}


def get_imp_pose(name: str) -> Pose:
    """Get an imp pose by name."""
    if name in IMP_POSES:
        return IMP_POSES[name]()
    raise ValueError(f"Unknown imp pose: {name}. Available: {list(IMP_POSES.keys())}")
