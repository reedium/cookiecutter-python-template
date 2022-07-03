from importlib.metadata import version

from .logger import create_logger

version = version("{{cookiecutter.package_name}}")

logger = create_logger(__package__)
