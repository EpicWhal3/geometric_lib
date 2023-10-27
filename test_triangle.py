import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_triangle_area(self):
        res = triangle.area(6, 21)
        self.assertEqual(res, 63)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_any_zero(self):
        res_a = triangle.perimeter(0, 6, 7)
        self.assertEqual(res_a, 0)

        res_b = triangle.perimeter(6, 0, 7)
        self.assertEqual(res_b, 0)

        res_c = triangle.perimeter(6, 7, 0)
        self.assertEqual(res_c, 0)
