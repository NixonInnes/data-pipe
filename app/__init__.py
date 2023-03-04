try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import os
import yaml
from config import config

from .settings import SettingsManager
from .repo_manager import RepoManager


Config = config.get(os.environ.get("ENV", "dev").lower())

settings = SettingsManager(Config.SETTINGS_DB)

def setup_settings():
    from .settings.required import required_settings
    
    with open("default-settings.yaml", 'r') as f:
        default_settings = yaml.load(f, Loader=yaml.FullLoader)
    
    configured_settings = settings.list()

    for setting, value in default_settings.items():
        if setting not in configured_settings:
            settings.set(setting, value)


from .utils import is_truthy

if is_truthy(os.environ.get("SETUP", "yes")):
    setup_settings()
    repo = RepoManager(settings["IMPORTS_DIR"], settings["IMPORTS_ADDRESS"])
    if not repo.exists():
        repo.clone()
else:
    repo = RepoManager(settings["IMPORTS_DIR"], settings["IMPORTS_ADDRESS"])
