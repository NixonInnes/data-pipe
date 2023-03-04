import os


class BaseConfig:
    SETTINGS_DB = os.environ.get("SETTINGS_DB", "sqlite:///settings.sqlite3")


class DevConfig(BaseConfig):
    SETTINGS_DB = os.environ.get("SETTINGS_DB", "sqlite:///dev-settings.sqlite3")


class TestConfig(BaseConfig):
    SETTINGS_DB = "sqlite:///test-settings.sqlite3"


class ProdConfig(BaseConfig):
    pass

config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
}