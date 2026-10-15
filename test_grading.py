
import unittest
from grading import calculate_grade


class TestGrading(unittest.TestCase):

    def test_grades(self):
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(72), "B")
        self.assertEqual(calculate_grade(55), "C")
        self.assertEqual(calculate_grade(32), "F")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(-1)

        with self.assertRaises(ValueError):
            calculate_grade(101)


if __name__ == "__main__":
    unittest.main()
