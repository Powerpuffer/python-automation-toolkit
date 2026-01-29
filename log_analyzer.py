import os

def analyze_log(log_file):
    if not os.path.exists(log_file):
        print(f"Error: Log file {log_file} does not exist.")
        return

    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(log_file, "r") as f:
        for line in f:
            for key in summary.keys():
                if key in line:
                    summary[key] += 1

    print("Log Analysis Summary:")
    for key, count in summary.items():
        print(f"{key}: {count}")

    # Optional: Save summary to a text file
    output_file = "log_summary.txt"
    with open(output_file, "w") as f:
        for key, count in summary.items():
            f.write(f"{key}: {count}\n")
    print(f"Summary saved to {output_file}")

if __name__ == "__main__":
    log_path = input("Enter full path to the log file: ")
    analyze_log(log_path)
