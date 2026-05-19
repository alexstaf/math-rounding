import math
import unittest

from math_rounding import math_rounding


class TestSpecialFloats(unittest.TestCase):
    def test_nan(self):
        n = float("nan")
        self.assertTrue(math.isnan(math_rounding(n)))
        self.assertTrue(math.isnan(math_rounding(n, 2)))

    def test_infinity(self):
        self.assertEqual(math_rounding(float("inf")), float("inf"))
        self.assertEqual(math_rounding(float("-inf")), float("-inf"))
        self.assertEqual(math_rounding(float("inf"), -1), float("inf"))
        self.assertEqual(math_rounding(float("-inf"), 3), float("-inf"))


class TestLargeNumbers(unittest.TestCase):
    def test_beyond_int64_range(self):
        self.assertEqual(math_rounding(1e20), 1e20)
        self.assertEqual(math_rounding(-1e20), -1e20)

    def test_near_int64_limit(self):
        n = 9.223372036854776e18
        self.assertEqual(math_rounding(n), n)

    def test_large_with_negative_precision(self):
        self.assertEqual(math_rounding(15, -1), 20.0)
        self.assertEqual(math_rounding(5e15, -1), 5e15)


if __name__ == "__main__":
    unittest.main()
