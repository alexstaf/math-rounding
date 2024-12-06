"""
Helper module to get package version.
"""

from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

PACKAGE_NAME = Path(__file__).parent.name

try:
    __version__ = version(PACKAGE_NAME)
except PackageNotFoundError:
    __version__ = '0.0.0 (source)'
