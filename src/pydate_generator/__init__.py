from .pydate_generator import *
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pydate_generator")
except PackageNotFoundError:
    # package is not installed
    pass