"""
Number rounding functions.
"""

from math import copysign
from numbers import Number

try:
    from numpy import astype, abs as _abs, copysign as _copysign
    from functools import partial
    _int = partial(lambda d, n: astype(n, d), int)
except ImportError:
    _int = int
    _abs = abs
    _copysign = copysign

try:
    from numba import njit as _njit
except ImportError:
    from dummy_decorator import dummy_decorator as _njit


@_njit
def math_rounding(n: Number, p: int = 0) -> float:
    assert isinstance(p, int)
    s = 10. ** p
    return _int(_copysign(_abs(n) * s + 0.5, n)) / s
