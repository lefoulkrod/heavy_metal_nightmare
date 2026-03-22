"""
Rigging system for Heavy Metal Nightmare.
"""

from rigging.parts import METAL_COLORS
from rigging.rig_builder import create_metal_warrior_rig
from rigging.poses import (
    get_idle_pose,
    get_walk_pose_1,
    get_walk_pose_2,
    get_attack_windup_pose,
    get_attack_strike_pose,
    get_pose,
    POSES,
)

__all__ = [
    'METAL_COLORS',
    'create_metal_warrior_rig',
    'get_idle_pose',
    'get_walk_pose_1',
    'get_walk_pose_2',
    'get_attack_windup_pose',
    'get_attack_strike_pose',
    'get_pose',
    'POSES',
]
