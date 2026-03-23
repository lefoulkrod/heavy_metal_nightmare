"""
Animation poses for the Metal Warrior character.

All poses use cumulative angles:
- shoulder + elbow + wrist = guitar orientation
- -90° = horizontal (for idle/walk)
- -180° = vertical, neck up
- 0° = vertical, neck down

Visibility:
- guitar_torso: shown for idle/walk (attached to torso)
- guitar_attack: shown for attack (attached to wrist)
"""

import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
from core.pose import Pose


def get_idle_pose():
    """Standing pose with guitar horizontal across body.
    
    Shows guitar_torso (attached to torso, horizontal playing position).
    Hides guitar_attack.
    """
    return Pose(
        name="idle",
        angles={
            "shoulder_left": 30,       # Left arm relaxed
            "elbow_left": -30,
            "wrist_left": 0,
            "shoulder_right": -30,     # Right arm to strum
            "elbow_right": -60,
            "wrist_right": -30,
            "hip_left": 0,
            "hip_right": 0,
            "neck": 0,
            "guitar_mount": -90,       # HORIZONTAL playing position (guitar across torso)
        },
        hidden_parts=["guitar_attack"]
    )


def get_walk_pose_1():
    """Walking pose - left leg forward.
    
    Shows guitar_torso (attached to torso, horizontal playing position).
    Hides guitar_attack.
    """
    return Pose(
        name="walk_1",
        angles={
            "shoulder_left": 30,
            "elbow_left": -30,
            "wrist_left": 0,
            "shoulder_right": -30,
            "elbow_right": -60,
            "wrist_right": -30,
            "hip_left": -20,
            "hip_right": 20,
            "neck": 3,
            "guitar_mount": -90,       # HORIZONTAL playing position
        },
        hidden_parts=["guitar_attack"]
    )


def get_walk_pose_2():
    """Walking pose - right leg forward.
    
    Shows guitar_torso (attached to torso, horizontal playing position).
    Hides guitar_attack.
    """
    return Pose(
        name="walk_2",
        angles={
            "shoulder_left": 30,
            "elbow_left": -30,
            "wrist_left": 0,
            "shoulder_right": -30,
            "elbow_right": -60,
            "wrist_right": -30,
            "hip_left": 20,
            "hip_right": -20,
            "neck": -3,
            "guitar_mount": -90,       # HORIZONTAL playing position
        },
        hidden_parts=["guitar_attack"]
    )


def get_attack_windup_pose():
    """Attack wind-up - guitar raised HIGH above head to chop down.
    
    Shows guitar_attack (attached to wrist, neck up position).
    Hides guitar_torso.
    
    Arm raised way back, guitar vertical with neck pointing UP.
    The body of the guitar hangs down, ready to chop.
    """
    return Pose(
        name="attack_windup",
        angles={
            "shoulder_left": -150,    # Left arm raised WAY back (behind head)
            "elbow_left": -120,       # Elbow bent sharply - guitar held high
            "wrist_left": 60,         # Wrist angled so guitar neck points UP
            "shoulder_right": 60,     # Right arm forward for balance
            "elbow_right": -30,
            "wrist_right": 0,
            "hip_left": -15,
            "hip_right": 15,
            "neck": -20,
            "guitar_mount": 0,        # Not visible anyway
        },
        hidden_parts=["guitar_torso"]
    )


def get_attack_strike_pose():
    """Attack strike - chopping DOWN with guitar.
    
    Shows guitar_attack (attached to wrist, body hitting position).
    Hides guitar_torso.
    
    Arm swung down hard, guitar body positioned to hit enemy.
    The body of the guitar (the "blade") swings down to strike.
    Cumulative angle around -45° to -90° (body angled down to strike).
    """
    return Pose(
        name="attack_strike",
        angles={
            "shoulder_left": 60,      # Left arm swung DOWN and forward
            "elbow_left": -90,        # Elbow extended for power swing
            "wrist_left": -60,        # Wrist angled so guitar body hits DOWN
            "shoulder_right": -45,    # Right arm back for follow-through
            "elbow_right": -30,
            "wrist_right": 30,
            "hip_left": 30,
            "hip_right": -30,
            "neck": -15,
            "guitar_mount": 0,        # Not visible anyway
        },
        hidden_parts=["guitar_torso"]
    )


# Pose library for easy access
POSES = {
    "idle": get_idle_pose,
    "walk_1": get_walk_pose_1,
    "walk_2": get_walk_pose_2,
    "attack_windup": get_attack_windup_pose,
    "attack_strike": get_attack_strike_pose,
}


def get_pose(name: str) -> Pose:
    """Get a pose by name."""
    if name in POSES:
        return POSES[name]()
    raise ValueError(f"Unknown pose: {name}. Available: {list(POSES.keys())}")