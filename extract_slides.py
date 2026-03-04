import fitz
import json
import sys
import re

def clean_text(text):
    lines = text.split("\n")

    cleaned = []
    for line in lines:
        line = line.strip()

        # Remove repeated header fragments
        if line.startswith("Devic"):
            continue
        if "CMPSC 311" in line:
            continue

        if line:
            cleaned.append(line)

    return cleaned

def extract_slides(pdf_path):
    doc = fitz.open(pdf_path)
    slides = []

    for i, page in enumerate(doc):
        raw_text = page.get_text("text")
        cleaned_lines = clean_text(raw_text)

        slides.append({
            "slide_number": i + 1,
            "lines": cleaned_lines
        })

    return slides

if __name__ == "__main__":
    slides = extract_slides(sys.argv[1])
    with open("slides.json", "w") as f:
        json.dump(slides, f, indent=2)