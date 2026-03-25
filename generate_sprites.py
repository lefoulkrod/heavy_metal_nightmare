#!/usr/bin/env python3
"""
Generate Metal Warrior sprites for Heavy Metal Nightmare.

Usage:
    python generate_sprites.py              # Generate all sprites
    python generate_sprites.py --pose idle  # Generate specific pose
"""

import sys
import os
import argparse

sys.path.insert(0, '/home/computron/pil_rigging_system')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.enhanced_rig import EnhancedRig
from core.optimized_rig import OptimizedRig
from rigging import create_metal_warrior_rig
from rigging.poses import (
    get_idle_pose,
    get_walk_pose_1,
    get_walk_pose_2,
    get_attack_windup_pose,
    get_attack_strike_pose,
)


def generate_all_sprites(output_dir: str = "sprites_metal_warrior", use_optimized: bool = True):
    """Generate all metal warrior sprites."""
    os.makedirs(output_dir, exist_ok=True)
    
    print("Metal Warrior Sprite Generator")
    print("=" * 50)
    if use_optimized:
        print("Using optimized rig (2.5x faster)")
    
    # Create base rig
    base_rig = create_metal_warrior_rig()
    
    # Use optimized or standard rig
    RigClass = OptimizedRig if use_optimized else EnhancedRig
    rig = RigClass(
        name=base_rig.name,
        root=base_rig.root,
        canvas_size=(base_rig.canvas_width, base_rig.canvas_height)
    )
    rig.root_position = (base_rig.root_x, base_rig.root_y)
    
    # Store original position
    original_root_pos = (base_rig.root_x, base_rig.root_y)
    
    sprites = []
    
    # Idle
    rig.reset()
    rig.root_position = original_root_pos
    rig.apply_pose_with_visibility(get_idle_pose())
    rig.center_in_canvas()
    rig.save(f"{output_dir}/player_idle.png")
    sprites.append("player_idle.png")
    print(f"✓ Generated: player_idle.png")
    
    # Walk cycle
    for i, pose_func in enumerate([get_walk_pose_1, get_walk_pose_2], 1):
        rig.reset()
        rig.root_position = original_root_pos
        rig.apply_pose_with_visibility(pose_func())
        rig.center_in_canvas()
        filename = f"player_walk{i}.png"
        rig.save(f"{output_dir}/{filename}")
        sprites.append(filename)
    print(f"✓ Generated: 2 walk frames")
    
    # Attack 1 - Wind-up
    rig.reset()
    rig.root_position = original_root_pos
    rig.apply_pose_with_visibility(get_attack_windup_pose())
    rig.center_in_canvas()
    rig.save(f"{output_dir}/player_attack1.png")
    sprites.append("player_attack1.png")
    print(f"✓ Generated: player_attack1.png (wind-up)")
    
    # Attack 2 - Strike
    rig.reset()
    rig.root_position = original_root_pos
    rig.apply_pose_with_visibility(get_attack_strike_pose())
    rig.center_in_canvas()
    rig.save(f"{output_dir}/player_attack2.png")
    sprites.append("player_attack2.png")
    print(f"✓ Generated: player_attack2.png (strike)")
    
    # Legacy attack (for compatibility)
    rig.reset()
    rig.root_position = original_root_pos
    rig.apply_pose_with_visibility(get_attack_strike_pose())
    rig.center_in_canvas()
    rig.save(f"{output_dir}/player_attack.png")
    sprites.append("player_attack.png")
    print(f"✓ Generated: player_attack.png")
    
    # Generate sprite sheet
    all_poses = [
        get_idle_pose(),
        get_walk_pose_1(),
        get_walk_pose_2(),
        get_attack_windup_pose(),
        get_attack_strike_pose()
    ]
    
    # Create sprite sheet manually since export_sprite_sheet expects dicts
    from PIL import Image as PILImage
    sheet_width = rig.canvas_width * 5
    sheet_height = rig.canvas_height
    sheet = PILImage.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))
    
    for i, pose in enumerate(all_poses):
        rig.reset()
        rig.root_position = original_root_pos
        rig.apply_pose_with_visibility(pose)
        sprite = rig.render()
        x = i * rig.canvas_width
        sheet.paste(sprite, (x, 0))
    
    sheet.save(f"{output_dir}/spritesheet.png")
    print(f"✓ Generated: spritesheet.png")
    
    print(f"\nComplete! {len(sprites)+1} files in: {output_dir}")
    return output_dir


def generate_single_pose(pose_name: str, output_dir: str = "sprites_metal_warrior"):
    """Generate a single pose for testing."""
    os.makedirs(output_dir, exist_ok=True)
    
    from rigging.poses import get_pose
    
    base_rig = create_metal_warrior_rig()
    rig = EnhancedRig(
        name=base_rig.name,
        root=base_rig.root,
        canvas_size=(base_rig.canvas_width, base_rig.canvas_height)
    )
    rig.root_position = (base_rig.root_x, base_rig.root_y)
    
    rig.reset()
    rig.apply_pose_with_visibility(get_pose(pose_name))
    rig.center_in_canvas()
    
    output_file = f"{output_dir}/test_{pose_name}.png"
    rig.save(output_file)
    print(f"✓ Generated: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate Metal Warrior sprites')
    parser.add_argument(
        '--pose',
        choices=['idle', 'walk_1', 'walk_2', 'attack_windup', 'attack_strike'],
        help='Generate a specific pose for testing'
    )
    parser.add_argument(
        '--output', '-o',
        default='sprites_metal_warrior',
        help='Output directory (default: sprites_metal_warrior)'
    )
    parser.add_argument(
        '--no-optimized',
        action='store_true',
        help='Use standard rig instead of optimized (for debugging)'
    )
    
    args = parser.parse_args()
    
    if args.pose:
        generate_single_pose(args.pose, args.output)
    else:
        generate_all_sprites(args.output, use_optimized=not args.no_optimized)


if __name__ == "__main__":
    main()
