import os
from config import config

from .settings import SettingsManager


Config = config.get(os.environ.get("ENV", "dev"))

settings = SettingsManager(Config.SETTINGS_DB)

