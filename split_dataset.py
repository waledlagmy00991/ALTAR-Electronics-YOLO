import os
import random
import shutil

# ================== الإعدادات ==================
BASE_DIR = "final"
TRAIN_RATIO = 0.8
# ===============================================

images_train = os.path.join(BASE_DIR, "images/train")
labels_train = os.path.join(BASE_DIR, "labels/train")

images_val = os.path.join(BASE_DIR, "images/val")
labels_val = os.path.join(BASE_DIR, "labels/val")

os.makedirs(images_val, exist_ok=True)
os.makedirs(labels_val, exist_ok=True)

# كل الصور
image_files = [
    f for f in os.listdir(images_train)
    if f.lower().endswith((".jpg", ".png", ".jpeg"))
]

random.shuffle(image_files)

split_index = int(len(image_files) * TRAIN_RATIO)
val_images = image_files[split_index:]

print(f"Total images: {len(image_files)}")
print(f"Validation images: {len(val_images)}")

for img in val_images:
    # نقل الصورة
    src_img = os.path.join(images_train, img)
    dst_img = os.path.join(images_val, img)
    shutil.move(src_img, dst_img)

    # نقل اللابل المقابل
    label_name = os.path.splitext(img)[0] + ".txt"
    src_lbl = os.path.join(labels_train, label_name)
    dst_lbl = os.path.join(labels_val, label_name)

    if os.path.exists(src_lbl):
        shutil.move(src_lbl, dst_lbl)

print("✅ Train / Val split done.")
