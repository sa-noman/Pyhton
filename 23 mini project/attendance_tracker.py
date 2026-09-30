import csv
from datetime import date
from pathlib import Path

def mark_attendance(path, name, status="present", day=None):
    day = day or date.today().isoformat()
    path = Path(path)
    new_file = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["date", "name", "status"])
        writer.writerow([day, name, status])

if __name__ == "__main__":
    mark_attendance("attendance.csv", input("Name: ").strip())
    print("Attendance saved.")
