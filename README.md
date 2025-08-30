---
title: Food Ingredient Scanner
emoji: 🍔
colorFrom: blue
colorTo: green
sdk: python
python_version: "3.11"
suggested_hardware: "t4-medium"  # GPU for PaddleOCR inference
suggested_storage: "small"     # enough for models + a few images
app_file: main.py
pinned: false
short_description: "Scan food images to detect ingredients and flag harmful additives"
tags: ["OCR", "FastAPI", "Food", "Ingredients", "Health"]
preload_from_hub:
  - paddleocr/models/ch_ppocr_server_v2.0  # Preload PaddleOCR model to speed up startup
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
