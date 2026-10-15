import unittest
import csv
import os
import tempfile
from grading import calculate_grade, generate_report, load_students


class TestGrading(unittest.TestCase):

    def test_boundary_values(self):
        test_cases = [
            (39, "F"),
            (40, "C"),
            (59, "C"),
            (60, "B"),
            (79, "B"),
            (80, "A"),
            (100, "A")
        ]

        for marks, expected in test_cases:
            with self.subTest(marks=marks):
                self.assertEqual(calculate_grade(marks), expected)

    def test_invalid_marks(self):
        for marks in [-1, 101]:
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_non_numeric_marks(self):
        for marks in ["hello", None, True]:
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_malformed_csv(self):
        with tempfile.NamedTemporaryFile(
            mode="w", newline="", suffix=".csv", delete=False
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["name", "marks"])
            writer.writerow(["Ravi", "85"])
            writer.writerow(["Priya"])
            filename = file.name

        try:
            with self.assertRaises(ValueError):
                load_students(filename)
        finally:
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()
