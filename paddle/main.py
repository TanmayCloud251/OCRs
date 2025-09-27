from paddleocr import PaddleOCR
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# ---------- Setup ----------
img_path = r"C:\Users\Acer\OneDrive\Desktop\OCRs\public\sample.jpg"

if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image not found: {img_path}")

# Initialize OCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Run OCR
result = ocr.predict(img_path)

# Extract data from result dictionary
ocr_data = result[0]
texts = ocr_data["rec_texts"]
scores = ocr_data["rec_scores"]
polys = ocr_data["rec_polys"]

# ---------- Print results ----------
print("\n📜 OCR Results:")
for i, (text, score) in enumerate(zip(texts, scores), 1):
    print(f"{i}. {text}  (Confidence: {score:.2f})")

# ---------- Drawing ----------
image = Image.open(img_path).convert("RGB")
draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
except:
    font = None

for text, score, poly in zip(texts, scores, polys):
    # Convert numpy array -> list of tuples
    box = [tuple(map(int, p)) for p in poly]

    # Draw polygon
    draw.polygon(box, outline="red", width=2)

    # Draw text label slightly above first point
    x, y = box[0]
    draw.text((x, y - 20), f"{text} ({score:.2f})", fill="blue", font=font)

# ---------- Save & Show ----------
out_path = "result_pillow.png"
image.save(out_path)
image.show()   # Opens the result image
print(f"\n✅ OCR result saved as {out_path} and opened for preview.")
