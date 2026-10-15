def calculate_grade(marks):
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise ValueError("Marks must be numeric")

    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks")

    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


def generate_report(students):
    for name, marks in students:
        grade = calculate_grade(marks)
        print(f"{name}: {grade}")
