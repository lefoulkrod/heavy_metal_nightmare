#!/usr/bin/env python3
"""Test to verify the pivot bug in rotation - with yellow dot on top."""

from PIL import Image, ImageDraw

def test_pivot_rotation():
    """Test pivot transformation during rotation."""
    
    # Create a simple test image: vertical rectangle with pivot at bottom
    width, height = 80, 130
    pivot_x, pivot_y = 0.5, 0.7  # Center horizontally, 70% down
    
    # Create a vertical rectangle (like the guitar)
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a simple shape to show orientation
    # Top part (neck) - red
    draw.rectangle([20, 0, 60, 50], fill=(255, 0, 0, 255))
    # Bottom part (body) - blue
    draw.rectangle([10, 50, 70, 130], fill=(0, 0, 255, 255))
    
    # Mark the pivot point on the original image
    pivot_px = int(width * pivot_x)
    pivot_py = int(height * pivot_y)
    draw.ellipse([pivot_px-5, pivot_py-5, pivot_px+5, pivot_py+5], fill=(0, 255, 0, 255))
    
    print(f"Original image: {width}x{height}")
    print(f"Pivot: ({pivot_x}, {pivot_y}) = pixel ({pivot_px}, {pivot_py})")
    
    # Rotate 90° counter-clockwise (angle = -90 in the rig system)
    angle = -90
    rotated = img.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)
    
    print(f"\nRotated image: {rotated.width}x{rotated.height}")
    
    # Target position for pivot
    target_x, target_y = 150, 100
    
    # The WRONG way (current code):
    wrong_paste_x = target_x - int(rotated.width * pivot_x)
    wrong_paste_y = target_y - int(rotated.height * pivot_y)
    
    # The CORRECT way (transformed pivot):
    new_pivot_x = 1 - pivot_y
    new_pivot_y = pivot_x
    
    correct_paste_x = target_x - int(rotated.width * new_pivot_x)
    correct_paste_y = target_y - int(rotated.height * new_pivot_y)
    
    print(f"\nWRONG calculation (current code):")
    print(f"  Using pivot ({pivot_x}, {pivot_y}) on rotated image")
    print(f"  paste_x = {target_x} - {rotated.width} * {pivot_x} = {wrong_paste_x}")
    print(f"  paste_y = {target_y} - {rotated.height} * {pivot_y} = {wrong_paste_y}")
    
    print(f"\nCORRECT calculation (transformed pivot):")
    print(f"  Transformed pivot: ({new_pivot_x}, {new_pivot_y})")
    print(f"  paste_x = {target_x} - {rotated.width} * {new_pivot_x} = {correct_paste_x}")
    print(f"  paste_y = {target_y} - {rotated.height} * {new_pivot_y} = {correct_paste_y}")
    
    # Create test canvases
    canvas_wrong = Image.new('RGBA', (300, 200), (128, 128, 128, 255))
    canvas_correct = Image.new('RGBA', (300, 200), (128, 128, 128, 255))
    
    # Paste using wrong calculation
    canvas_wrong.paste(rotated, (wrong_paste_x, wrong_paste_y), rotated)
    
    # Paste using correct calculation
    canvas_correct.paste(rotated, (correct_paste_x, correct_paste_y), rotated)
    
    # Draw target pivot marker (yellow) AFTER pasting
    draw_wrong = ImageDraw.Draw(canvas_wrong)
    draw_correct = ImageDraw.Draw(canvas_correct)
    draw_wrong.ellipse([target_x-5, target_y-5, target_x+5, target_y+5], fill=(255, 255, 0, 255), outline=(0, 0, 0))
    draw_correct.ellipse([target_x-5, target_y-5, target_x+5, target_y+5], fill=(255, 255, 0, 255), outline=(0, 0, 0))
    
    # Add labels
    draw_wrong.text((10, 10), "WRONG: Using original pivot", fill=(255, 0, 0, 255))
    draw_wrong.text((10, 25), "Yellow = target pivot", fill=(255, 255, 0, 255))
    draw_wrong.text((10, 40), "Green = actual pivot on shape", fill=(0, 255, 0, 255))
    
    draw_correct.text((10, 10), "CORRECT: Transformed pivot", fill=(0, 255, 0, 255))
    draw_correct.text((10, 25), "Yellow = target pivot", fill=(255, 255, 0, 255))
    draw_correct.text((10, 40), "Green = actual pivot on shape", fill=(0, 255, 0, 255))
    
    canvas_wrong.save('/home/computron/heavy_metal_nightmare/test_wrong.png')
    canvas_correct.save('/home/computron/heavy_metal_nightmare/test_correct.png')
    
    print(f"\nSaved test_wrong.png and test_correct.png")
    print("\nThe yellow dot is the target pivot position.")
    print("The green dot on the shape is the actual pivot point.")
    print("If they align, the pivot transformation is correct.")

if __name__ == '__main__':
    test_pivot_rotation()