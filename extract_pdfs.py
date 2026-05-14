import fitz
import os

pdf_paths = [
    r"H:\My Drive\25-26 Máster en Formación Permanente en Teaching\Teaching & Learning with Technology in Classrooms\Assignments\Antonio Tagaruma - Assignment 1.pdf",
    r"H:\My Drive\25-26 Máster en Formación Permanente en Teaching\Teaching & Learning with Technology in Classrooms\Assignments\Antonio Tagaruma - Assignment 2.pdf",
    r"H:\My Drive\25-26 Máster en Formación Permanente en Teaching\Teaching & Learning with Technology in Classrooms\Assignments\Antonio Tagaruma - Assignment 3.pdf",
    r"H:\My Drive\25-26 Máster en Formación Permanente en Teaching\Teaching & Learning with Technology in Classrooms\Assignments\TeachingLearningTechnology2026(1).pdf"
]

output_dir = r"c:\Users\Anton\Desktop\OLD FILES\GOALS\AI\GitHub 2025\techineducation"

for path in pdf_paths:
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        base_name = os.path.basename(path).replace(".pdf", ".txt")
        out_path = os.path.join(output_dir, base_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted {base_name}")
    except Exception as e:
        print(f"Error reading {path}: {e}")
