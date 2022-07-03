from pydantic import (
    BaseModel,
    BaseSettings,
)


class SubModel(BaseModel):
    foo: str = "bar"


class Config(BaseSettings):
    api_key: str = "EXAMPLEKEY"
    more_settings: SubModel = SubModel()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def entry_point():
    config = Config()


if __name__ == "__main__":
    entry_point()
