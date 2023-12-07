import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            res = circle.area(0)

    def test_area_calc(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, 78.5, 1)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(0)

    def test_length_calc(self):
        res = circle.perimeter(8)
        self.assertAlmostEqual(res, 50.2, 1)
