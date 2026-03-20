from PIL import Image, ImageDraw

# Colors
C_SKIN = (240, 200, 180, 255)
C_HAIR = (200, 40, 40, 255)
C_HAIR_DARK = (150, 30, 30, 255)
C_HAIR_LIGHT = (255, 80, 80, 255)
C_BLACK = (30, 30, 30, 255)
C_LEATHER = (45, 45, 45, 255)
C_STUD = (200, 200, 210, 255)
C_GUITAR = (220, 50, 50, 255)
C_GUITAR_DARK = (160, 35, 35, 255)
C_WOOD = (160, 110, 60, 255)
C_SILVER = (220, 220, 230, 255)
C_BOOT = (50, 40, 35, 255)

def create(w, h):
    return Image.new('RGBA', (w, h), (0, 0, 0, 0))

# === HAIR BACK - longer, flows down ===
hair_back = create(34, 50)
draw = ImageDraw.Draw(hair_back)
# Long flowing back hair
draw.rectangle([0, 0, 34, 50], fill=C_HAIR_DARK)
draw.rectangle([4, 0, 30, 45], fill=C_HAIR)
# Highlights
draw.rectangle([6, 5, 8, 40], fill=C_HAIR_LIGHT)
draw.rectangle([26, 5, 28, 40], fill=C_HAIR_LIGHT)
hair_back.save('/home/computron/generated_images/parts/v3_hair_back.png')

# === HAIR FRONT/BANGS - higher up, doesn't cover eyes ===
hair_front = create(26, 10)
draw = ImageDraw.Draw(hair_front)
# Just the top part, above eyes
draw.rectangle([0, 0, 26, 10], fill=C_HAIR)
draw.rectangle([2, 2, 6, 8], fill=C_HAIR_LIGHT)
draw.rectangle([20, 2, 24, 8], fill=C_HAIR_LIGHT)
hair_front.save('/home/computron/generated_images/parts/v3_hair_front.png')

# === SAME OTHER COMPONENTS FROM V2 ===
import shutil
shutil.copy('/home/computron/generated_images/parts/v2_head.png', '/home/computron/generated_images/parts/v3_head.png')
shutil.copy('/home/computron/generated_images/parts/v2_guitar.png', '/home/computron/generated_images/parts/v3_guitar.png')
shutil.copy('/home/computron/generated_images/parts/v2_torso.png', '/home/computron/generated_images/parts/v3_torso.png')
shutil.copy('/home/computron/generated_images/parts/v2_arm_left.png', '/home/computron/generated_images/parts/v3_arm_left.png')
shutil.copy('/home/computron/generated_images/parts/v2_arm_right.png', '/home/computron/generated_images/parts/v3_arm_right.png')
shutil.copy('/home/computron/generated_images/parts/comp_leg.png', '/home/computron/generated_images/parts/v3_leg.png')

print("Created v3 components")
print("Hair front raised so eyes are visible")
