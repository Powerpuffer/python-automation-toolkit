# Python Automation Toolkit

A collection of Python scripts designed to automate common tasks such as file organization, PDF and Word conversions, CSV to SQLite data management, and log analysis. This toolkit improves productivity by handling repetitive tasks efficiently and providing a menu-driven interface for ease of use.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)


## Features

This toolkit currently includes the following scripts:

- **csv_to_sqlite.py**  
  Imports CSV files into an SQLite database (`students.db`). Handles multiple CSV files and ensures structured data for querying and analysis.

- **fileorganizer.py**  
  Organizes files in a directory by type or extension into corresponding folders (e.g., PDF, Word, Excel).

- **log_analyzer.py**  
  Analyzes log files (`log_summary.txt`) and generates summaries of errors, counts, or activity over time.

- **menu.py**  
  Provides a menu-driven interface to launch any of the available scripts interactively.

- **pdf_to_word.py**  
  Converts PDF files in the `pdf/` folder into editable Word documents.

- **word_to_pdf.py**  
  Converts Word documents into PDF format.

---

## Installation

1. Ensure you have **Python 3.10+** installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/python-automation-toolkit.git
Navigate to the project folder:

cd python-automation-toolkit
Install required Python packages:

pip install -r requirements.txt
Recommended packages: pandas, python-docx, PyPDF2, sqlite3 (standard with Python).

Usage
You can run scripts individually:

python csv_to_sqlite.py
python fileorganizer.py
python log_analyzer.py
python pdf_to_word.py
python word_to_pdf.py
Or use the menu interface:

python menu.py
The menu allows you to select any task interactively without running individual scripts manually.

Folder Structure
python-automation-toolkit/
│
├── pdf/                   ← Source PDF files
├── sampledata/            ← Sample CSV, Word, or PDF files for testing
├── csv_to_sqlite.py       ← Script to import CSVs to SQLite
├── fileorganizer.py       ← Script to organize files by type
├── log_analyzer.py        ← Script to analyze logs
├── log_summary.txt        ← Example log summary output
├── menu.py                ← Menu-driven interface for all scripts
├── pdf_to_word.py         ← Convert PDFs to Word documents
├── word_to_pdf.py         ← Convert Word documents to PDF
├── students.db            ← SQLite database created by CSV import
└── README.md              ← This project documentation
Dependencies
Install required Python packages:

pip install pandas python-docx PyPDF2