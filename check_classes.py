import os
from collections import Counter

LABELS_DIR = "final/labels/train"

counter = Counter()

for file in os.listdir(LABELS_DIR):
    if not file.endswith(".txt"):
        continue

    with open(os.path.join(LABELS_DIR, file), "r") as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                counter[int(parts[0])] += 1

print("Class distribution:")
for k in sorted(counter.keys()):
    print(f"Class {k}: {counter[k]} boxes")
