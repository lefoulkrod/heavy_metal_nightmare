"""
Rigging system for the Imp enemy in Heavy Metal Nightmare.

The Imp is a small flying demon with:
- Red body with black horns
- Yellow eyes with black pupils
- Purple bat-like wings
- Small arms with claws
- Thin legs
- Curled tail with black tip
"""

from rigging.imp.parts import IMP_COLORS
from rigging.imp.rig_builder import create_imp_rig
from rigging.imp.poses import (
    get_imp_idle_pose,
    get_imp_float1_pose,
    get_imp_float2_pose,
    get_imp_attack_pose,
    get_imp_pose,
    IMP_POSES,
)

__all__ = [
    'IMP_COLORS',
    'create_imp_rig',
    'get_imp_idle_pose',
    'get_imp_float1_pose',
    'get_imp_float2_pose',
    'get_imp_attack_pose',
    'get_imp_pose',
    'IMP_POSES',
]
