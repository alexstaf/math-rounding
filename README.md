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
