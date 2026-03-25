#!/usr/bin/env python3
"""
Imp Enemy Sprite Generator for Heavy Metal Nightmare.

Generates 4 sprites using the PIL rigging system:
- enemy_imp_idle.png   - Wings folded, hovering
- enemy_imp_attack.png - Forward lunge, claws extended
- enemy_imp_fly1.png   - Wings up (flap cycle peak)
- enemy_imp_fly2.png   - Wings down (flap cycle trough)

Usage:
    cd /home/computron/repos/heavy_metal_nightmare
    python rigging/imp/generate_sprites.py
    
    # Or with custom output directory:
    python rigging/imp/generate_sprites.py /path/to/output

Requirements:
    - pil_rigging_system at /home/computron/repos/pil_rigging_system
    - heavy_metal_nightmare rigging modules
"""

import sys
import os
from pathlib import Path


# =============================================================================
# PATH SETUP
# =============================================================================
def setup_paths() -> bool:
    """
    Set up Python paths for imports.
    
    Returns:
        True if paths are set up successfully, False otherwise.
    """
    try:
        # Add pil_rigging_system to path
        pil_rigging_path = Path("/home/computron/repos/pil_rigging_system")
        if not pil_rigging_path.exists():
            print(f"ERROR: PIL rigging system not found at {pil_rigging_path}")
            return False
        
        sys.path.insert(0, str(pil_rigging_path))
        
        # Add heavy_metal_nightmare to path
        hmn_path = Path("/home/computron/repos/heavy_metal_nightmare")
        if not hmn_path.exists():
            print(f"ERROR: Heavy Metal Nightmare repo not found at {hmn_path}")
            return False
            
        sys.path.insert(0, str(hmn_path))
        
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to set up paths: {e}")
        return False


# =============================================================================
# IMPORTS (after path setup)
# =============================================================================
def import_modules():
    """
    Import required modules after paths are set up.
    
    Returns:
        Tuple of (OptimizedRig, create_imp_rig, pose_functions, ImportError or None)
    """
    try:
        # Import PIL rigging system
        from core.optimized_rig import OptimizedRig
        
        # Import imp rigging modules
        from rigging.imp.rig_builder import create_imp_rig
        from rigging.imp.poses import (
            get_imp_idle_pose,
            get_imp_attack_pose,
            get_imp_float1_pose,
            get_imp_float2_pose,
            get_imp_pose,
            IMP_POSES,
        )
        
        pose_functions = {
            "idle": get_imp_idle_pose,
            "attack": get_imp_attack_pose,
            "float1": get_imp_float1_pose,
            "float2": get_imp_float2_pose,
        }
        
        return OptimizedRig, create_imp_rig, pose_functions, None
        
    except ImportError as e:
        return None, None, None, e


# =============================================================================
# SPRITE GENERATION
# =============================================================================
def create_optimized_imp_rig(create_imp_rig_func, OptimizedRigClass):
    """
    Create an OptimizedRig from the standard imp rig.
    
    Args:
        create_imp_rig_func: Function to create the base imp rig
        OptimizedRigClass: OptimizedRig class to wrap the rig
        
    Returns:
        OptimizedRig instance ready for sprite generation
        
    Raises:
        RuntimeError: If rig creation fails
    """
    try:
        # Create the base rig
        base_rig = create_imp_rig_func()
        
        # Wrap in OptimizedRig for better performance
        optimized = OptimizedRigClass(
            name=base_rig.name,
            root=base_rig.root,
            canvas_size=(base_rig.canvas_width, base_rig.canvas_height)
        )
        
        # Copy position settings
        optimized.root_x = base_rig.root_x
        optimized.root_y = base_rig.root_y
        
        # Enable rotation caching for performance
        optimized.enable_cache()
        
        return optimized
        
    except Exception as e:
        raise RuntimeError(f"Failed to create optimized imp rig: {e}")


def generate_imp_sprites(
    output_dir: str = None,
    poses_to_generate: list = None
) -> list:
    """
    Generate all Imp sprites using the PIL rigging system.
    
    Args:
        output_dir: Directory to save sprites to. If None, uses default.
        poses_to_generate: List of pose names to generate. 
                          If None, generates all default poses.
                          
    Returns:
        List of paths to generated sprite files
        
    Raises:
        RuntimeError: If sprite generation fails
        ValueError: If invalid pose names are provided
    """
    # Set up paths
    if not setup_paths():
        raise RuntimeError("Failed to set up Python paths")
    
    # Import modules
    OptimizedRig, create_imp_rig, pose_functions, import_error = import_modules()
    
    if import_error:
        raise RuntimeError(f"Failed to import required modules: {import_error}")
    
    # Set default output directory
    if output_dir is None:
        output_dir = Path("/home/computron/repos/heavy_metal_nightmare/sprites_imp")
    else:
        output_dir = Path(output_dir)
    
    # Ensure output directory exists
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Failed to create output directory {output_dir}: {e}")
    
    # Default poses to generate
    default_poses = [
        ("idle", pose_functions["idle"], "enemy_imp_idle.png"),
        ("attack", pose_functions["attack"], "enemy_imp_attack.png"),
        ("float1", pose_functions["float1"], "enemy_imp_fly1.png"),
        ("float2", pose_functions["float2"], "enemy_imp_fly2.png"),
    ]
    
    # Filter poses if specified
    if poses_to_generate is not None:
        valid_poses = set(pose_functions.keys())
        invalid_poses = set(poses_to_generate) - valid_poses
        
        if invalid_poses:
            raise ValueError(
                f"Invalid pose names: {invalid_poses}. "
                f"Available: {list(valid_poses)}"
            )
        
        default_poses = [
            (name, func, filename) 
            for name, func, filename in default_poses 
            if name in poses_to_generate
        ]
    
    print(f"Generating Imp sprites to: {output_dir}")
    print("-" * 50)
    
    # Create the optimized rig
    try:
        rig = create_optimized_imp_rig(create_imp_rig, OptimizedRig)
    except RuntimeError as e:
        raise RuntimeError(f"Rig creation failed: {e}")
    
    print(f"Created rig: {rig.name}")
    print(f"Canvas size: {rig.canvas_width}x{rig.canvas_height}")
    print(f"Number of parts: {len(rig.root.get_all_parts())}")
    print()
    
    generated_files = []
    errors = []
    
    # Generate each pose
    for pose_name, pose_func, filename in default_poses:
        print(f"Generating {pose_name}...", end=" ")
        
        try:
            # Reset rig to default state
            rig.reset()
            
            # Get pose data
            pose = pose_func()
            
            # Apply root offset from pose
            rig.root_x = 50 + pose.root_offset[0]
            rig.root_y = 55 + pose.root_offset[1]
            
            # Apply pose with visibility using the proper method
            rig.apply_pose_with_visibility(pose)
            
            # Render the sprite
            img = rig.render()
            
            # Save the sprite
            filepath = output_dir / filename
            img.save(filepath)
            generated_files.append(str(filepath))
            
            print(f"✓ Saved: {filepath}")
            
        except Exception as e:
            errors.append((pose_name, str(e)))
            print(f"✗ FAILED: {e}")
    
    # Report results
    print()
    print("-" * 50)
    
    if errors:
        print(f"WARNING: {len(errors)} pose(s) failed:")
        for pose_name, error_msg in errors:
            print(f"  - {pose_name}: {error_msg}")
        print()
    
    print(f"Successfully generated {len(generated_files)} sprites:")
    for f in generated_files:
        print(f"  - {f}")
    print()
    print("Done!")
    
    return generated_files


# =============================================================================
# MAIN
# =============================================================================
def main():
    """Main entry point for the sprite generator."""
    print("=" * 60)
    print("Heavy Metal Nightmare - Imp Sprite Generator")
    print("=" * 60)
    print()
    
    # Parse command line arguments
    output_dir = None
    poses = None
    
    if len(sys.argv) > 1:
        # First argument is output directory
        output_dir = sys.argv[1]
        
    if len(sys.argv) > 2:
        # Additional arguments are pose names
        poses = sys.argv[2:]
    
    try:
        generated = generate_imp_sprites(output_dir, poses)
        
        if generated:
            print(f"\nSuccess! Generated {len(generated)} sprites.")
            return 0
        else:
            print("\nWarning: No sprites were generated.")
            return 1
            
    except ValueError as e:
        print(f"\nError: Invalid input - {e}")
        return 1
        
    except RuntimeError as e:
        print(f"\nError: {e}")
        return 1
        
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
