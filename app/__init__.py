try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

import os
from config import config

from .settings import SettingsManager
from .repo_manager import RepoManager


Config = config.get(os.environ.get("ENV", "dev").lower())

settings = SettingsManager(Config.SETTINGS_DB)
repo = RepoManager(settings)


from .utils import is_truthy

if is_truthy(os.environ.get("SETUP", "yes")):
    settings.load_yaml("default-settings.yaml")
    if not repo.exists():
        repo.clone()
