import math
import unittest

from math_rounding import math_rounding

try:
    import numpy as np
except ImportError:
    np = None


class TestReadmeExamples(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(math_rounding(0.5), 1.0)
        self.assertEqual(math_rounding(-0.5), -1.0)
        self.assertEqual(math_rounding(1.1), 1.0)
        self.assertEqual(math_rounding(0.05, 1), 0.1)
        self.assertEqual(math_rounding(5, -1), 10.0)
        self.assertEqual(math_rounding(15, -1), 20.0)


class TestMathematicalRounding(unittest.TestCase):
    def test_half_away_from_zero(self):
        self.assertEqual(math_rounding(1.5), 2.0)
        self.assertEqual(math_rounding(-1.5), -2.0)
        self.assertEqual(math_rounding(2.5), 3.0)
        self.assertEqual(math_rounding(-2.5), -3.0)

    def test_negative_zero_sign(self):
        self.assertTrue(math.copysign(1, math_rounding(-0.0)) == -1.0)
        self.assertTrue(math.copysign(1, math_rounding(-0.3)) == -1.0)

    def test_positive_zero(self):
        self.assertEqual(math_rounding(0.0), 0.0)
        self.assertTrue(math.copysign(1, math_rounding(0.0)) == 1.0)


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


@unittest.skipIf(np is None, "numpy is not installed")
class TestNumpyScalars(unittest.TestCase):
    def test_uses_numpy_ufuncs(self):
        import math_rounding.rounding as rounding_mod

        self.assertIs(rounding_mod._abs, np.abs)
        self.assertIs(rounding_mod._copysign, np.copysign)

    def test_float64_rounding(self):
        self.assertEqual(math_rounding(np.float64(0.5)), 1.0)
        self.assertEqual(math_rounding(np.float64(-0.5)), -1.0)
        self.assertEqual(math_rounding(np.float64(1.1)), 1.0)
        self.assertEqual(math_rounding(np.float64(0.05), 1), 0.1)

    def test_float64_negative_zero(self):
        self.assertTrue(math.copysign(1, math_rounding(np.float64(-0.0))) == -1.0)
        self.assertTrue(math.copysign(1, math_rounding(np.float64(-0.3))) == -1.0)

    def test_float64_special_values(self):
        self.assertTrue(math.isnan(math_rounding(np.float64("nan"))))
        self.assertEqual(math_rounding(np.float64("inf")), np.inf)
        self.assertEqual(math_rounding(np.float64("-inf")), -np.inf)

    def test_float64_large_numbers(self):
        self.assertEqual(math_rounding(np.float64(1e20)), np.float64(1e20))
        self.assertEqual(math_rounding(np.float64(-1e20)), np.float64(-1e20))


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
