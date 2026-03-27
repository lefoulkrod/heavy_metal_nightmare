#!/usr/bin/env python3
"""
Regenerate all player sprites for Heavy Metal Nightmare.
Creates 5 poses: idle, walk1, walk2, attack_windup, attack_strike

Usage:
    python regenerate_sprites.py
"""

import sys
import os

# Add the pil_rigging_system to path
sys.path.insert(0, '/home/computron/pil_rigging_system')

# Import the rig builder and poses
from rigging.rig_builder import create_metal_warrior_rig
from rigging.poses import (
    get_idle_pose,
    get_walk_pose_1,
    get_walk_pose_2,
    get_attack_windup_pose,
    get_attack_strike_pose,
)
from PIL import Image


def regenerate_sprites():
    """Regenerate all player sprites for the Heavy Metal Warrior."""
    
    # Output directory for player sprites
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sprites', 'player')
    os.makedirs(output_dir, exist_ok=True)
    
    # Define poses to generate with their filenames
    poses = [
        ('idle', get_idle_pose, 'player_idle.png'),
        ('walk1', get_walk_pose_1, 'player_walk1.png'),
        ('walk2', get_walk_pose_2, 'player_walk2.png'),
        ('attack_windup', get_attack_windup_pose, 'player_attack_windup.png'),
        ('attack_strike', get_attack_strike_pose, 'player_attack_strike.png'),
    ]
    
    generated_files = []
    images = []
    
    print("=" * 60)
    print("Heavy Metal Nightmare - Sprite Regeneration")
    print("=" * 60)
    print(f"\nCanvas size: 200x250")
    print(f"Output directory: {output_dir}")
    print()
    
    for pose_name, pose_func, filename in poses:
        print(f"Generating {pose_name}...")
        
        # Create a fresh rig for each pose
        rig = create_metal_warrior_rig()
        
        # Get the pose object
        pose = pose_func()
        
        # Apply the pose with visibility settings
        rig.apply_pose_with_visibility(pose)
        
        # Render the rig (canvas size is already set in rig: 200x250)
        img = rig.render()
        
        # Save the image
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        generated_files.append(filepath)
        images.append(img)
        
        print(f"  Saved: {filename}")
        
        # Verify guitar visibility settings
        guitar_torso = rig.get_part("guitar_torso")
        guitar_attack = rig.get_part("guitar_attack")
        if guitar_torso and guitar_attack:
            if pose_name in ('idle', 'walk1', 'walk2'):
                print(f"  guitar_torso: visible, guitar_attack: hidden")
            else:
                print(f"  guitar_torso: hidden, guitar_attack: visible")
    
    # Generate spritesheet
    print("\n" + "-" * 60)
    print("Creating player_spritesheet.png...")
    
    # Spritesheet: 5 frames horizontal
    canvas_width = 200
    canvas_height = 250
    spritesheet = Image.new('RGBA', (canvas_width * 5, canvas_height), (0, 0, 0, 0))
    
    for i, img in enumerate(images):
        # Center the image in the frame
        x_offset = i * canvas_width + (canvas_width - img.width) // 2
        y_offset = (canvas_height - img.height) // 2
        spritesheet.paste(img, (x_offset, y_offset), img)
    
    spritesheet_path = os.path.join(output_dir, 'player_spritesheet.png')
    spritesheet.save(spritesheet_path)
    generated_files.append(spritesheet_path)
    print(f"  Saved: player_spritesheet.png ({spritesheet.size[0]}x{spritesheet.size[1]})")
    
    print("\n" + "=" * 60)
    print("Regeneration complete!")
    print(f"Total files generated: {len(generated_files)}")
    print("=" * 60)
    
    return generated_files


if __name__ == '__main__':
    files = regenerate_sprites()
    print("\nGenerated files:")
    for f in files:
        print(f"  - {f}")
