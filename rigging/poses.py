"""
Animation poses for the Metal Warrior character.

All poses use cumulative angles:
- shoulder + elbow + wrist = guitar orientation
- -90° = horizontal (for idle/walk)
- -180° = vertical, neck up
- 0° = vertical, neck down
"""


def get_idle_pose():
    """Standing pose with guitar horizontal across body."""
    # Cumulative: 30 + (-30) + (-90) = -90° (horizontal)
    return {
        "shoulder_left": 30,       # Arm reaches across
        "elbow_left": -30,        # Elbow bent
        "wrist_left": -90,        # Guitar horizontal
        "shoulder_right": -30,    # Right arm to strum
        "elbow_right": -60, 
        "wrist_right": -30,
        "hip_left": 0, 
        "hip_right": 0, 
        "neck": 0
    }


def get_walk_pose_1():
    """Walking pose - left leg forward."""
    return {
        "shoulder_left": 30, 
        "elbow_left": -30, 
        "wrist_left": -90,        # Guitar horizontal
        "shoulder_right": -30, 
        "elbow_right": -60, 
        "wrist_right": -30,
        "hip_left": -20, 
        "hip_right": 20, 
        "neck": 3
    }


def get_walk_pose_2():
    """Walking pose - right leg forward."""
    return {
        "shoulder_left": 30, 
        "elbow_left": -30, 
        "wrist_left": -90,        # Guitar horizontal
        "shoulder_right": -30, 
        "elbow_right": -60, 
        "wrist_right": -30,
        "hip_left": 20, 
        "hip_right": -20, 
        "neck": -3
    }


def get_attack_windup_pose():
    """Attack wind-up - guitar raised HIGH above head to chop down.
    
    Arm raised way back, guitar vertical with neck pointing UP.
    """
    return {
        "shoulder_left": -120,     # Left arm raised WAY back
        "elbow_left": -90,         # Elbow bent sharply up
        "wrist_left": 30,          # Adjust for vertical guitar
        "shoulder_right": 80,      # Right arm raised
        "elbow_right": -45, 
        "wrist_right": 0,
        "hip_left": -15, 
        "hip_right": 15, 
        "neck": -30
    }


def get_attack_strike_pose():
    """Attack strike - chopping DOWN with guitar.
    
    Arm swung down hard, guitar vertical with neck pointing DOWN.
    """
    return {
        "shoulder_left": 80,       # Left arm swung DOWN hard
        "elbow_left": -45,         # Elbow bent
        "wrist_left": -45,         # Guitar vertical, neck DOWN
        "shoulder_right": -60,     # Right arm forward
        "elbow_right": -30, 
        "wrist_right": 60,
        "hip_left": 40, 
        "hip_right": -40, 
        "neck": -20
    }


# Pose library for easy access
POSES = {
    "idle": get_idle_pose,
    "walk_1": get_walk_pose_1,
    "walk_2": get_walk_pose_2,
    "attack_windup": get_attack_windup_pose,
    "attack_strike": get_attack_strike_pose,
}


def get_pose(name: str) -> dict:
    """Get a pose by name."""
    if name in POSES:
        return POSES[name]()
    raise ValueError(f"Unknown pose: {name}. Available: {list(POSES.keys())}")
