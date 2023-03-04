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


from .utils import is_truthy

do_setup = is_truthy(os.environ.get("SETUP", "yes"))

if do_setup:
    settings.load_yaml("default-settings.yaml")

repo = RepoManager(settings["IMPORTS_DIR"], settings["IMPORTS_ADDRESS"])

if do_setup:
    if not repo.exists():
        repo.clone()
