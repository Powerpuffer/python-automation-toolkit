from docx import Document
from fpdf import FPDF
import os

def docx_to_pdf(docx_file, pdf_file):
    """
    Converts a .docx file to a .pdf using pure Python.
    Works without Microsoft Word installed.
    """
    if not os.path.exists(docx_file):
        print(f"Error: Word file {docx_file} does not exist.")
        return

    doc = Document(docx_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:  # skip empty paragraphs
            pdf.multi_cell(0, 10, text)

    # Ensure output folder exists
    output_dir = os.path.dirname(pdf_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    pdf.output(pdf_file)
    print(f"PDF saved to {pdf_file}")

if __name__ == "__main__":
    docx_path = input("Enter full path to Word file (.docx): ")
    output_path = input("Enter output PDF path (include filename): ")
    docx_to_pdf(docx_path, output_path)
