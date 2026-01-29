from docx2pdf import convert
import os

def convert_word_to_pdf(word_file, output_folder=None):
    if not os.path.exists(word_file):
        print(f"Error: Word file {word_file} does not exist.")
        return

    try:
        if output_folder:
            os.makedirs(output_folder, exist_ok=True)
            convert(word_file, output_folder)
            print(f"Converted {word_file} to PDF in {output_folder}")
        else:
            convert(word_file)
            print(f"Converted {word_file} to PDF in the same folder")
    except Exception as e:
        print(f"Conversion failed: {e}")

if __name__ == "__main__":
    word_path = input("Enter full path to the Word file (.docx): ")
    output_dir = input("Enter output folder for PDF (press Enter for same folder): ")
    output_dir = output_dir if output_dir.strip() != "" else None
    convert_word_to_pdf(word_path, output_dir)
