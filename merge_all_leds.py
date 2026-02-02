import os
import shutil

# ================== الإعدادات ==================

# فولدرات داتا الليدات (عدّل الأسماء لو مختلفة)
SOURCE_DATASETS = [
    "raw/LED",   # Anode / Cathode
    "raw/Leds2",   # LED colors / defective
    "raw/Leds3"    # Casing / Node
]

DEST_IMAGES = "final/images/train"
DEST_LABELS = "final/labels/train"

# أي class في الداتا دي -> LED = 4
LED_CLASS_ID = 4

# ===============================================

os.makedirs(DEST_IMAGES, exist_ok=True)
os.makedirs(DEST_LABELS, exist_ok=True)

def process_dataset(source_dataset):
    images_dir = os.path.join(source_dataset, "train/images")
    labels_dir = os.path.join(source_dataset, "train/labels")

    if not os.path.exists(labels_dir):
        print(f"❌ labels folder not found in {source_dataset}")
        return

    label_files = os.listdir(labels_dir)
    print(f"📂 Processing {source_dataset} | labels: {len(label_files)}")

    for label_file in label_files:
        label_path = os.path.join(labels_dir, label_file)

        with open(label_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue

            # أي class -> LED
            parts[0] = str(LED_CLASS_ID)
            new_lines.append(" ".join(parts))

        if not new_lines:
            continue

        image_base = os.path.splitext(label_file)[0]
        found_image = None

        for ext in [".jpg", ".png", ".jpeg"]:
            candidate = os.path.join(images_dir, image_base + ext)
            if os.path.exists(candidate):
                found_image = candidate
                break

        if not found_image:
            print("⚠️ image not found for:", label_file)
            continue

        shutil.copy(found_image, DEST_IMAGES)

        with open(os.path.join(DEST_LABELS, label_file), "w") as f:
            f.write("\n".join(new_lines))


for ds in SOURCE_DATASETS:
    process_dataset(ds)

print("✅ All LED datasets merged successfully.")
