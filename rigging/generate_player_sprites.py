#!/usr/bin/env python3
"""
Generate Heavy Metal Warrior player sprites using the rigging system.
Creates 5 poses: idle, walk_1, walk_2, attack_windup, attack_strike
"""

import sys
import os

# Add the pil_rigging_system to path
sys.path.insert(0, '/home/computron/pil_rigging_system')

# Add rigging module path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rigging.rig_builder import create_metal_warrior_rig
from rigging.poses import (
    get_idle_pose,
    get_walk_pose_1,
    get_walk_pose_2,
    get_attack_windup_pose,
    get_attack_strike_pose,
)
from PIL import Image


def generate_sprites():
    """Generate all player sprites for the Heavy Metal Warrior."""
    
    # Output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sprites', 'player')
    os.makedirs(output_dir, exist_ok=True)
    
    # Define poses to generate
    poses = [
        ('idle', get_idle_pose, 'player_idle.png'),
        ('walk_1', get_walk_pose_1, 'player_walk1.png'),
        ('walk_2', get_walk_pose_2, 'player_walk2.png'),
        ('attack_windup', get_attack_windup_pose, 'player_attack_windup.png'),
        ('attack_strike', get_attack_strike_pose, 'player_attack_strike.png'),
    ]
    
    generated_files = []
    images = []
    
    print("Generating Heavy Metal Warrior sprites...")
    print("=" * 50)
    
    for pose_name, pose_func, filename in poses:
        print(f"\nGenerating {pose_name} pose...")
        
        # Create a fresh rig for each pose
        rig = create_metal_warrior_rig()
        
        # Get the pose object
        pose = pose_func()
        
        # Apply the pose with visibility settings
        rig.apply_pose_with_visibility(pose)
        
        # Render the rig
        img = rig.render()
        
        # Save the image
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        generated_files.append(filepath)
        images.append(img)
        
        print(f"  Saved: {filepath}")
        print(f"  Size: {img.size}")
        
        # Debug: show visibility status
        guitar_torso = rig.get_part("guitar_torso")
        guitar_attack = rig.get_part("guitar_attack")
        if guitar_torso:
            print(f"  guitar_torso visible: {guitar_torso.visible}")
        if guitar_attack:
            print(f"  guitar_attack visible: {guitar_attack.visible}")
    
    # Create spritesheet
    print("\n" + "=" * 50)
    print("Creating spritesheet...")
    
    # Spritesheet: 5 frames horizontal
    frame_width = 200
    frame_height = 250
    spritesheet = Image.new('RGBA', (frame_width * 5, frame_height), (0, 0, 0, 0))
    
    for i, img in enumerate(images):
        # Center the image in the frame
        x_offset = i * frame_width + (frame_width - img.width) // 2
        y_offset = (frame_height - img.height) // 2
        spritesheet.paste(img, (x_offset, y_offset), img)
    
    spritesheet_path = os.path.join(output_dir, 'player_spritesheet.png')
    spritesheet.save(spritesheet_path)
    generated_files.append(spritesheet_path)
    print(f"  Saved: {spritesheet_path}")
    print(f"  Size: {spritesheet.size}")
    
    print("\n" + "=" * 50)
    print("Generation complete!")
    print(f"Total files generated: {len(generated_files)}")
    
    return generated_files


if __name__ == '__main__':
    files = generate_sprites()
    print("\nGenerated files:")
    for f in files:
        print(f"  - {f}")