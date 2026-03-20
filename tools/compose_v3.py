from PIL import Image

def load(name):
    return Image.open(f'/home/computron/generated_images/parts/v3_{name}.png')

guitar = load('guitar')
head = load('head')
torso = load('torso')
hair_back = load('hair_back')
hair_front = load('hair_front')
leg = load('leg')
arm_left = load('arm_left')
arm_right = load('arm_right')

def paste_centered(dest, src, cx, cy):
    w, h = src.size
    x = int(cx - w / 2)
    y = int(cy - h / 2)
    dest.paste(src, (x, y), src)
    return dest

def rotate(img, angle):
    if angle == 0:
        return img
    return img.rotate(-angle, resample=Image.BICUBIC, expand=True)

# === IDLE ===
idle = Image.new('RGBA', (80, 80), (0, 0, 0, 0))

paste_centered(idle, hair_back, 40, 30)

paste_centered(idle, leg, 32, 65)
paste_centered(idle, leg, 48, 65)

paste_centered(idle, torso, 40, 50)

arm_l = rotate(arm_left, -20)
paste_centered(idle, arm_l, 28, 45)

paste_centered(idle, guitar, 40, 52)

arm_r = rotate(arm_right, 15)
paste_centered(idle, arm_r, 52, 45)

paste_centered(idle, head, 40, 24)  # Slightly lower head position

paste_centered(idle, hair_front, 40, 14)  # Hair higher up

idle.save('/home/computron/generated_images/parts/v3_idle.png')
print("Created v3_idle.png")

# === WALK 1 ===
walk1 = Image.new('RGBA', (80, 80), (0, 0, 0, 0))

paste_centered(walk1, hair_back, 40, 29)

leg_l = rotate(leg, -15)
paste_centered(walk1, leg_l, 28, 62)
leg_r = rotate(leg, 10)
paste_centered(walk1, leg_r, 48, 67)

paste_centered(walk1, torso, 40, 49)

arm_l = rotate(arm_left, -25)
paste_centered(walk1, arm_l, 28, 44)

paste_centered(walk1, guitar, 40, 51)

arm_r = rotate(arm_right, 20)
paste_centered(walk1, arm_r, 52, 44)

paste_centered(walk1, head, 40, 23)
paste_centered(walk1, hair_front, 40, 13)

walk1.save('/home/computron/generated_images/parts/v3_walk1.png')
print("Created v3_walk1.png")

# === WALK 2 ===
walk2 = Image.new('RGBA', (80, 80), (0, 0, 0, 0))

paste_centered(walk2, hair_back, 40, 29)

leg_l = rotate(leg, 10)
paste_centered(walk2, leg_l, 28, 67)
leg_r = rotate(leg, -15)
paste_centered(walk2, leg_r, 48, 62)

paste_centered(walk2, torso, 40, 49)

arm_l = rotate(arm_left, -30)
paste_centered(walk2, arm_l, 28, 44)

paste_centered(walk2, guitar, 40, 51)

arm_r = rotate(arm_right, 25)
paste_centered(walk2, arm_r, 52, 44)

paste_centered(walk2, head, 40, 23)
paste_centered(walk2, hair_front, 40, 13)

walk2.save('/home/computron/generated_images/parts/v3_walk2.png')
print("Created v3_walk2.png")

# === ATTACK - Guitar swung UP and FORWARD ===
attack = Image.new('RGBA', (80, 80), (0, 0, 0, 0))

paste_centered(attack, hair_back, 42, 27)

leg_l = rotate(leg, -10)
paste_centered(attack, leg_l, 32, 65)
leg_r = rotate(leg, 10)
paste_centered(attack, leg_r, 50, 65)

torso_rot = rotate(torso, -5)
paste_centered(attack, torso_rot, 42, 48)

# ATTACK POSE: Guitar swung up-forward like a weapon
# Left arm forward holding neck
arm_l = rotate(arm_left, 45)
paste_centered(attack, arm_l, 35, 38)

# Guitar - rotated UP (negative angle = pointing up-right)
gr = rotate(guitar, -45)
paste_centered(attack, gr, 48, 38)

# Right arm back for power
arm_r = rotate(arm_right, -30)
paste_centered(attack, arm_r, 55, 45)

paste_centered(attack, head, 42, 22)
paste_centered(attack, hair_front, 42, 12)

attack.save('/home/computron/generated_images/parts/v3_attack.png')
print("Created v3_attack.png")
print("Attack pose: guitar now points UP and FORWARD")

print("\nAll v3 poses complete!")
