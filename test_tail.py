#!/usr/bin/env python3
"""Debug script to check tail visibility"""

import sys
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
sys.path.insert(0, '/home/computron/repos/heavy_metal_nightmare')

from rigging.imp.rig_builder import create_imp_rig

# Create the rig
rig = create_imp_rig()

# List all parts
print("Parts in rig:")
for part in rig.root.get_all_parts():
    print(f"  - {part.name}: z_index={part.z_index}, visible={part.visible}")

# Find the tail
tail = rig.get_part("tail")
if tail:
    print(f"\nTail found!")
    print(f"  z_index: {tail.z_index}")
    print(f"  visible: {tail.visible}")
    print(f"  width: {tail.width}, height: {tail.height}")
    print(f"  pivot: ({tail.pivot_x}, {tail.pivot_y})")
else:
    print("\nTail NOT found!")

# Check tail_base joint
tail_joint = rig.get_joint("tail_base")
if tail_joint:
    print(f"\nTail base joint:")
    print(f"  angle: {tail_joint.angle}")
    print(f"  position: ({tail_joint.x}, {tail_joint.y})")
    print(f"  child: {tail_joint.child.name if tail_joint.child else 'None'}")
else:
    print("\nTail base joint NOT found!")

# Render and save with joints visible
print("\nRendering with joints visible...")
img = rig.render(show_joints=True)
img.save('/home/computron/repos/heavy_metal_nightmare/sprites_imp/debug_tail.png')
print("Saved debug image to: sprites_imp/debug_tail.png")

# Also render without joints
img2 = rig.render(show_joints=False)
img2.save('/home/computron/repos/heavy_metal_nightmare/sprites_imp/debug_tail_no_joints.png')
print("Saved debug image (no joints) to: sprites_imp/debug_tail_no_joints.png")
