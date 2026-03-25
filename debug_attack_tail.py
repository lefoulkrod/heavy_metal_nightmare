#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
sys.path.insert(0, '/home/computron/repos/heavy_metal_nightmare')

from rigging.imp.rig_builder import create_imp_rig
from rigging.imp.poses import get_imp_attack_pose

# Create the rig
rig = create_imp_rig()

# Get attack pose
pose = get_imp_attack_pose()
print(f"Attack pose root offset: {pose.root_offset}")
print(f"Attack pose tail_base angle: {pose.angles.get('tail_base', 'NOT SET')}")

# Apply pose
rig.root_x = 50 + pose.root_offset[0]
rig.root_y = 55 + pose.root_offset[1]
rig.apply_pose(pose.angles)

# Render and save
img = rig.render(show_joints=False)
img.save('/home/computron/repos/heavy_metal_nightmare/sprites_imp/debug_attack.png')
print("Saved debug_attack.png")

# Also render with joints
img2 = rig.render(show_joints=True)
img2.save('/home/computron/repos/heavy_metal_nightmare/sprites_imp/debug_attack_joints.png')
print("Saved debug_attack_joints.png")
