import csv
import sqlite3
import os

DB_NAME = "students.db"

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_num INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            cell_number TEXT
        )
    """)
    conn.commit()

def import_csv_to_db(csv_file):
    if not os.path.exists(csv_file):
        print(f"Error: CSV file {csv_file} does not exist.")
        return

    conn = sqlite3.connect(DB_NAME)
    create_table(conn)
    cursor = conn.cursor()

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cursor.execute("""
                    INSERT INTO students (student_num, first_name, last_name, email, cell_number)
                    VALUES (?, ?, ?, ?, ?)
                """, (row['student_num'], row['first_name'], row['last_name'], row['email'], row['cell_number']))
            except sqlite3.IntegrityError as e:
                print(f"Skipping duplicate or invalid entry: {row} ({e})")

    conn.commit()
    conn.close()
    print(f"CSV data imported successfully into {DB_NAME}")

if __name__ == "__main__":
    csv_path = input("Enter full path to CSV file: ")
    import_csv_to_db(csv_path)
