import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = square.area(0)

    def test_area_calc(self):
        res = square.area(6)
        self.assertEqual(res, 36)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(0)

    def test_perimeter_calc(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
