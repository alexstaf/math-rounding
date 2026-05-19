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


if __name__ == "__main__":
    unittest.main()
