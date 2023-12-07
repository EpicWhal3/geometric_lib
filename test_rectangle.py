import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        with self.assertRaises(ValueError):
            res_1 = rectangle.area(10, 0)
            res_2 = rectangle.area(0, 10)
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_summ(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimeter(0, 0)
    def test_perimeter_summ(self):
        res = rectangle.perimeter(15, 6)
        self.assertEqual(res, 42)
