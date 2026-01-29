import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    """
    Runs a Python script in the same folder using subprocess.
    """
    script_path = os.path.join(os.getcwd(), script_name)
    if not os.path.exists(script_path):
        print(f"Script {script_name} not found!")
        return
    subprocess.run(["python", script_path], check=True)

def main():
    while True:
        clear_screen()
        print("=== Python Automation Toolkit ===")
        print("1. File Organizer")
        print("2. CSV → SQLite Importer")
        print("3. Log File Analyzer")
        print("4. Word → PDF (requires Word)")
        print("5. PDF → Word")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            run_script("fileorganizer.py")
        elif choice == "2":
            run_script("csv_to_sqlite.py")
        elif choice == "3":
            run_script("log_analyzer.py")
        elif choice == "4":
            run_script("word_to_pdf.py")
        elif choice == "5":
            run_script("pdf_to_word.py")
        elif choice == "0":
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Press Enter to try again.")
            input()

if __name__ == "__main__":
    main()
