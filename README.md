# Mathematical rounding in Python

This package has one purpose: fast mathematical rounding of numbers.

## Installation

Use the following command to install the package:

```bash
pip install math-rounding
```

The package can use `numba` to increase speed of the calculations.
If you want to install it with numba, you can use the following command:

```bash
pip install math-rounding[numba]
```

or just install `numba` separately.

## Usage

The main function of the package `math_rounding` has the following signature:

```py
def math_rounding(n: Number, p: int = 0) -> float:
    ...
```
where:
* `n` is the number to round;
* `p` is integer number that specifies the position to which rounding will be performed.

`p` could be a positive number or a negative number. It represents the position in the number from the dot:
* when it's equal to `0` (*default*), the rounding will be performed to integer;
* when it's positive, it represents the position in fractional part of the number;
* when it's negative, it represents the position in integer part of the number.

### Example

```py
from math_rounding import math_rounding

print(math_rounding(0.5))      # 1.0
print(math_rounding(-0.5))     # -1.0
print(math_rounding(1.1))      # 1.0
print(math_rounding(0.05, 1))  # 0.1
print(math_rounding(5, -1))    # 10.0
print(math_rounding(15, -1))   # 20.0
```

### Tests

```bash
pip install -e ".[numba]"
python -m unittest discover -s tests -v
```

## Limitations

The function is optimized for typical `float` values and precision values. It uses IEEE-754 `float` arithmetic and (with `numba` installed) JIT-compiled code. Outside the ranges below, results may be wrong or an exception may be raised.

### Precision `p`

`p` is the exponent in the scale factor `10**p`. For a 64-bit `float`:

| Range | What happens |
|-------|----------------|
| **Recommended:** about `-15` … `15` | Stable for most numbers; matches the examples above. |
| **`p` ≥ 309** | `10**p` overflows in Python; behavior is undefined. |
| **`p` around 307–308** | `10**p` is finite, but `abs(n) * 10**p` can overflow to `inf` for ordinary `n`, which may yield `nan`. |
| **`p` ≤ -324** | `10**p` underflows to `0.0`; dividing by `s` raises `ZeroDivisionError`. |
| **`p` around -308 … -323** | `10**p` is tiny; for many `n` the value `abs(n) * 10**p + 0.5` is dominated by `0.5`, so the result can be far from the expected rounded value. |

If you need extreme `p`, check the result or use another tool (for example `decimal.Decimal`).

### Value `n`

| Case | Behavior |
|------|----------|
| **`nan`, `±inf`** | Returned unchanged. |
| **Very large \|n\|** (roughly above `10**18` with default `p=0`) | Safe with the current implementation; much larger values are still subject to `float` precision limits. |
| **Negative zero** (`-0.0`) | Sign is preserved when the rounded result is zero. |
| **Binary floating-point** | Values such as `2.675` at `p=2` may not match pen-and-paper decimal rounding because `n` is not stored exactly in base 10. |
