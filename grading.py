import csv


def calculate_grade(marks):
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise ValueError("Marks must be numeric")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


def load_students(filename):
    students = []

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None or not {"name", "marks"}.issubset(reader.fieldnames):
            raise ValueError("CSV must contain name and marks columns")

        for row in reader:
            if not row.get("name") or not row.get("marks"):
                raise ValueError("Malformed CSV record")

            try:
                marks = float(row["marks"])
            except ValueError:
                raise ValueError("Marks must be numeric")

            calculate_grade(marks)
            students.append((row["name"], marks))

    return students


def generate_report(students):
    for name, marks in students:
        grade = calculate_grade(marks)
        print(f"{name}: {grade}")
