from doctr.models import ocr_predictor
from doctr.io import DocumentFile


model = ocr_predictor(pretrained=True)


img_path = r"C:\Users\Acer\OneDrive\Desktop\OCRs\public\sample.jpg"
doc = DocumentFile.from_images([img_path])


result = model(doc)


for page in result.pages:
    for block in page.blocks:
        for line in block.lines:
            line_text = " ".join([word.value for word in line.words])
            print(f"{line_text}")
