#!/usr/bin/env python3
"""Debug script to trace guitar rendering."""

import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
sys.path.insert(0, '/home/computron/heavy_metal_nightmare')

from rigging.rig_builder import create_metal_warrior_rig
from rigging.poses import get_idle_pose
from PIL import Image

# Create rig
rig = create_metal_warrior_rig()

# Get the pose
pose = get_idle_pose()

print("=== POSE DATA ===")
print(f"Pose name: {pose.name}")
print(f"Angles: {pose.angles}")
print(f"Hidden parts: {pose.hidden_parts}")

# Apply pose
rig.apply_pose_with_visibility(pose)

print("\n=== JOINT ANGLES AFTER APPLY ===")
def print_joints(part, indent=0):
    prefix = "  " * indent
    print(f"{prefix}{part.name} (visible={part.visible})")
    for joint in part.joints:
        print(f"{prefix}  Joint '{joint.name}': angle={joint.angle}°")
        if joint.child:
            print_joints(joint.child, indent + 2)

print_joints(rig.root)

print("\n=== GUITAR_TORSO INFO ===")
guitar_torso = rig.get_part("guitar_torso")
if guitar_torso:
    print(f"Name: {guitar_torso.name}")
    print(f"Size: {guitar_torso.width}x{guitar_torso.height}")
    print(f"Pivot: ({guitar_torso.pivot_x}, {guitar_torso.pivot_y})")
    print(f"Pivot offset: ({guitar_torso.pivot_offset_x}, {guitar_torso.pivot_offset_y})")
    print(f"Visible: {guitar_torso.visible}")

print("\n=== GUITAR_MOUNT JOINT INFO ===")
guitar_mount = rig.get_joint("guitar_mount")
if guitar_mount:
    print(f"Joint name: {guitar_mount.name}")
    print(f"Joint angle: {guitar_mount.angle}°")
    print(f"Joint default_angle: {guitar_mount.default_angle}°")
    print(f"Joint position on parent: ({guitar_mount.rel_x}, {guitar_mount.rel_y})")
    print(f"Joint absolute position: ({guitar_mount.x}, {guitar_mount.y})")

# Render with joint markers
print("\n=== RENDERING WITH JOINT MARKERS ===")
img = rig.render(show_joints=True)
img.save('/home/computron/heavy_metal_nightmare/debug_joints.png')
print("Saved debug image to debug_joints.png")

# Also render without markers
img2 = rig.render(show_joints=False)
img2.save('/home/computron/heavy_metal_nightmare/debug_no_joints.png')
print("Saved debug image to debug_no_joints.png")