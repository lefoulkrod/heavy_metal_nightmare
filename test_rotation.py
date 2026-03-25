#!/usr/bin/env python3
"""Test guitar rotation to verify horizontal orientation."""

import sys
sys.path.insert(0, '/home/computron/pil_rigging_system')
sys.path.insert(0, '/home/computron/heavy_metal_nightmare')

from PIL import Image, ImageDraw
from rigging.parts import create_guitar

def test_guitar_rotation():
    """Test guitar rotation at different angles."""
    
    # Create guitar with pivot at body (for idle/walk poses)
    guitar = create_guitar(
        "test_guitar",
        body_width=45,
        body_height=60,
        neck_length=50,
        pivot_at_neck=False
    )
    
    print(f"Guitar dimensions: {guitar.width}x{guitar.height}")
    print(f"Pivot: ({guitar.pivot_x}, {guitar.pivot_y})")
    print(f"Pivot offset: ({guitar.pivot_offset_x}, {guitar.pivot_offset_y})")
    
    # Create a test canvas
    canvas_width = 300
    canvas_height = 200
    
    # Test different angles
    angles = [0, -45, -90, -135, -180]
    
    for angle in angles:
        img = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Get guitar image
        guitar_img = guitar.get_image()
        
        # Rotate if needed
        if angle != 0:
            guitar_img = guitar_img.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)
        
        # Calculate position to center the pivot point
        pivot_x = canvas_width // 2
        pivot_y = canvas_height // 2
        
        paste_x = int(pivot_x - guitar_img.width * guitar.pivot_x)
        paste_y = int(pivot_y - guitar_img.height * guitar.pivot_y)
        
        img.paste(guitar_img, (paste_x, paste_y), guitar_img)
        
        # Draw pivot point marker
        draw.ellipse([pivot_x-5, pivot_y-5, pivot_x+5, pivot_y+5], fill=(255, 0, 0, 128))
        
        # Draw label
        draw.text((10, 10), f"Angle: {angle}°", fill=(255, 255, 255, 255))
        
        # Save
        filename = f'/home/computron/heavy_metal_nightmare/test_rotation_{angle}.png'
        img.save(filename)
        print(f"Saved: {filename}")
    
    # Also create a reference showing what "horizontal" should look like
    print("\n=== ROTATION DIRECTION REFERENCE ===")
    print("In PIL Image.rotate():")
    print("  - Positive angles rotate COUNTER-CLOCKWISE")
    print("  - Negative angles rotate CLOCKWISE")
    print("")
    print("Guitar drawn with neck at TOP (y=0), body at BOTTOM (y=height)")
    print("")
    print("For guitar_mount angle = -90:")
    print("  - Code does: img.rotate(-angle) = img.rotate(90)")
    print("  - 90° COUNTER-CLOCKWISE rotation")
    print("  - Neck (was at top) -> moves to LEFT")
    print("  - Body (was at bottom) -> moves to RIGHT")
    print("  - Result: HORIZONTAL guitar with neck pointing LEFT")
    print("")
    print("This should be correct for a 'playing' position!")

if __name__ == '__main__':
    test_guitar_rotation()