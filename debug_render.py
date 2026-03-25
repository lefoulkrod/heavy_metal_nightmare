#!/usr/bin/env python3
"""Debug the actual rendering to trace angles."""

import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
sys.path.insert(0, '/home/computron/heavy_metal_nightmare')

from rigging.rig_builder import create_metal_warrior_rig
from rigging.poses import get_idle_pose
from PIL import Image

# Monkey-patch the render method to add debugging
original_collect = None

def debug_collect_parts(self, part, x, y, angle, render_list):
    """Debug version of _collect_parts_recursive."""
    indent = "  " * len([p for p in render_list])
    print(f"{indent}{part.name}: pos=({x:.1f}, {y:.1f}), angle={angle:.1f}°, visible={part.visible}")
    
    if part.visible:
        render_list.append((part, x, y, angle))
    
    for joint in part.joints:
        if joint.child:
            # Calculate child's position based on joint
            joint_x = x + (joint.x - part.pivot_offset_x)
            joint_y = y + (part.height * joint.rel_y - part.pivot_offset_y)
            
            print(f"{indent}  Joint '{joint.name}': rel=({joint.rel_x}, {joint.rel_y}), "
                  f"abs=({joint.x}, {joint.y}), angle={joint.angle}°")
            
            # Apply rotation to joint position
            if angle != 0:
                import math
                rad = math.radians(angle)
                rel_x = joint.x - part.pivot_offset_x
                rel_y = joint.y - part.pivot_offset_y
                rot_x = rel_x * math.cos(rad) - rel_y * math.sin(rad)
                rot_y = rel_x * math.sin(rad) + rel_y * math.cos(rad)
                joint_x = x + rot_x
                joint_y = y + rot_y
            
            # Recurse to child with joint's angle added
            debug_collect_parts(self, joint.child, joint_x, joint_y, angle + joint.angle, render_list)

# Create rig
rig = create_metal_warrior_rig()
pose = get_idle_pose()

print("=== APPLYING POSE ===")
print(f"Pose angles: {pose.angles}")
print(f"Hidden parts: {pose.hidden_parts}")

rig.apply_pose_with_visibility(pose)

print("\n=== RENDERING (with angle trace) ===")
render_list = []
debug_collect_parts(rig, rig.root, rig.root_x, rig.root_y, 0, render_list)

print("\n=== FINAL RENDER LIST (sorted by z_index) ===")
for part, x, y, angle in sorted(render_list, key=lambda item: item[0].z_index):
    print(f"  {part.name}: pos=({x:.1f}, {y:.1f}), angle={angle:.1f}°")

# Now render
img = rig.render()
img.save('/home/computron/heavy_metal_nightmare/debug_final.png')
print("\nSaved debug_final.png")