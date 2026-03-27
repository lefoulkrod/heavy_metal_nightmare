#!/usr/bin/env python3
"""
Standalone script to generate Imp enemy sprites.

Generates 4 sprites:
- imp_idle.png      - Wings folded, hovering
- imp_float1.png    - Wings up (flap peak)
- imp_float2.png    - Wings down (flap trough)
- imp_attack.png    - Forward lunge, claws extended

Usage:
    cd /home/computron/repos/heavy_metal_nightmare
    python rigging/imp/generate_imp_sprites.py
"""

import sys
import os

# Add paths
sys.path.insert(0, '/home/computron/repos/pil_rigging_system')
sys.path.insert(0, '/home/computron/repos/heavy_metal_nightmare')

from rigging.imp.rig_builder import create_imp_rig
from rigging.imp.poses import (
    get_imp_idle_pose,
    get_imp_float1_pose,
    get_imp_float2_pose,
    get_imp_attack_pose,
)


def generate_imp_sprites(output_dir: str = None):
    """Generate all Imp sprites."""
    
    # Default output directory
    if output_dir is None:
        output_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "sprites/imp"
        )
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Generating Imp sprites to: {output_dir}")
    print("-" * 50)
    
    # Create the rig
    rig = create_imp_rig()
    print(f"Created rig: {rig.name}")
    print(f"Canvas size: {rig.canvas_width}x{rig.canvas_height}")
    print(f"Number of parts: {len(rig.root.get_all_parts())}")
    print()
    
    # Define poses to generate
    poses = [
        ("idle", get_imp_idle_pose, "imp_idle.png"),
        ("float1", get_imp_float1_pose, "imp_float1.png"),
        ("float2", get_imp_float2_pose, "imp_float2.png"),
        ("attack", get_imp_attack_pose, "imp_attack.png"),
    ]
    
    generated_files = []
    
    for pose_name, pose_func, filename in poses:
        print(f"Generating {pose_name}...")
        
        # Reset rig
        rig.reset()
        
        # Get pose
        pose = pose_func()
        
        # Apply root offset
        rig.root_x = 50 + pose.root_offset[0]
        rig.root_y = 55 + pose.root_offset[1]
        
        # Apply pose angles
        rig.apply_pose(pose.angles)
        
        # Apply visibility (if any parts are hidden)
        for part_name in pose.hidden_parts:
            rig.set_part_visibility(part_name, False)
        
        # Render
        img = rig.render()
        
        # Save
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        generated_files.append(filepath)
        
        print(f"  Saved: {filepath}")
    
    print()
    print("-" * 50)
    print(f"Generated {len(generated_files)} sprites:")
    for f in generated_files:
        print(f"  - {f}")
    print()
    print("Done!")
    
    return generated_files


if __name__ == "__main__":
    # Allow custom output directory from command line
    output_dir = sys.argv[1] if len(sys.argv) > 1 else None
    generate_imp_sprites(output_dir)
