"""
Number rounding functions.
"""

from math import copysign
from numbers import Number

try:
    from numba import njit as _njit
except ImportError:
    from dummy_decorator import dummy_decorator as _njit


@_njit
def math_rounding(n: Number, p: int = 0) -> float:
    assert isinstance(p, int)
    s = 10. ** p
    return int(copysign(abs(n) * s + 0.5, n)) / s
