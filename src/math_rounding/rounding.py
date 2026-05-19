"""
Number rounding functions.
"""

from math import copysign, isinf, isnan
from numbers import Number

try:
    from numpy import abs as _abs, copysign as _copysign
except ImportError:
    _abs = abs
    _copysign = copysign

try:
    from numba import njit as _njit
except ImportError:
    from dummy_decorator import dummy_decorator as _njit


@_njit
def math_rounding(n: Number, p: int = 0) -> float:
    assert isinstance(p, int)
    if isnan(n) or isinf(n):
        return n
    s = 10. ** p
    return _copysign((_abs(n) * s + 0.5) // 1.0 / s, n)
