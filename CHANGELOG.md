# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Unit tests for `numpy.float64` values (behavior matches earlier releases for typical scalar inputs).
- CI job `test-without-numpy` that installs the package without optional dependencies (NumPy-specific tests are skipped).

### Changed

- When NumPy is installed, use `numpy.abs` and `numpy.copysign` instead of built-in functions; otherwise fall back to `abs` and `copysign` from `math` (no change in results for typical `float` and `numpy.float64` inputs).

## [1.0.2] - 2026-05-19

### Added

- README section describing valid ranges for `p` and `n`.
- Unit tests and a CI job to run them.

### Fixed

- Preserve the sign of negative zero when the rounded result is zero.
- Return `nan` and `±inf` unchanged.
- Avoid incorrect results for very large `|n|` when using Numba (use `// 1.0` instead of `int()`).

## [1.0.1] - 2024-12-06

### Fixed

- Project dependencies.

## [1.0.0] - 2024-12-06

### Added

- 1st version of the package which can round decimal fractions to the specified position an use `numba` to increase calculation speed.

[1.0.2]: https://github.com/alexstaf/math-rounding/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/alexstaf/math-rounding/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/alexstaf/math-rounding/releases/tag/1.0.0
