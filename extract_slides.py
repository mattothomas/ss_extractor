import fitz  # pymupdf
import json
import sys

def extract_slides(pdf_path):
    doc = fitz.open(pdf_path)
    slides = []

    for i, page in enumerate(doc):
        text = page.get_text("text")
        slides.append({
            "slide_number": i + 1,
            "content": text.strip()
        })

    return slides

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    slides = extract_slides(pdf_path)

    with open("slides.json", "w") as f:
        json.dump(slides, f, indent=2)

    print(f"Extracted {len(slides)} slides.")