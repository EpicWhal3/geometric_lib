import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        with self.assertRaises(ValueError):
            res_1 = triangle.area(10, 0)
            res_2 = triangle.area(0, 10)
    def test_triangle_area(self):
        res = triangle.area(6, 21)
        self.assertEqual(res, 63)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(0, 0, 0)

    def test_any_zero(self):
        with self.assertRaises(ValueError):
            res_a = triangle.perimeter(0, 6, 7)
            res_b = triangle.perimeter(6, 0, 7)
            res_c = triangle.perimeter(6, 7, 0)
    def test_perimiteter_summ(self):
        res = triangle.perimeter(5, 8, 13)
        self.assertEqual(res, 26)

    def test_negative(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(-1, -2, -3)
