import argparse

from pydantic import (
    BaseModel,
    BaseSettings,
)

from {{cookiecutter.package_name}} import version


class SubModel(BaseModel):
    foo: str = "bar"


class Config(BaseSettings):
    api_key: str = "EXAMPLEKEY"
    more_settings: SubModel = SubModel()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="""
        {{cookiecutter.package_description}}
        """,
    )
    parser.add_argument(
        "--version", action="version", version=f"package_name {version}"
    )

    return parser.parse_args()


def entry_point():
    args = parse_arguments()
    config = Config()


if __name__ == "__main__":
    entry_point()
