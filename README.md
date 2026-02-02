
# ALTAR-Electronics-YOLO

YOLOv8 dataset configuration and training code for detecting electronic components:
Arduino, Battery, Breadboard, Resistor, LED, and Wire.

> ⚠️ **Note:**  
> Due to GitHub size limits, the dataset is hosted externally and is **not included** in this repository.

---
📥 Dataset Download

The dataset is hosted on Google Drive.

🔗 Download link:
https://drive.google.com/drive/folders/156NTDuLRl55sh_9FlFgPSWHvhDfIFize?usp=drive_link

How to use the dataset:

Download the dataset from the link above

Extract it (if compressed)

Rename the extracted folder to final

Place it in the root directory of this repository

Your project structure should look like this:
ALTAR-Electronics-YOLO/
├─ final/
│  ├─ images/
│  │  ├─ train/
│  │  └─ val/
│  └─ labels/
│     ├─ train/
│     └─ val/
├─ data.yaml
├─ yolov8n.pt
├─ check_classes.py
├─ split_dataset.py
├─ merge_all_leds.py
├─ .gitignore
└─ README.md


## 📦 Requirements

- Python 3.9+
- ultralytics

Install dependencies:
```bash
pip install ultralytics

