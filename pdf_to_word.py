import pdfplumber
from docx import Document
import os

def pdf_to_word(pdf_file, word_file):
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file {pdf_file} does not exist.")
        return

    doc = Document()
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                doc.add_paragraph(text)

    doc.save(word_file)
    print(f"Word document saved to {word_file}")

if __name__ == "__main__":
    pdf_path = input("Enter full path to PDF file: ")
    output_path = input("Enter output Word file path (include filename): ")
    pdf_to_word(pdf_path, output_path)
