import os

from config import Config
from app import PipePieces, repo_manager

Config.GIT_DIR = "tests/imports"
Config.refresh_modules()


def clean_repo():
    if os.path.exists(Config.GIT_DIR):
        os.system(f"rm -rf {Config.GIT_DIR}")


def test_repo_manager():
    clean_repo()
    assert not os.path.exists(Config.GIT_DIR)
    repo_manager.clone()
    assert os.path.exists(Config.GIT_DIR)
    assert os.path.exists(Config.PIPE_COMBINER_MODULE)
    assert os.path.exists(Config.PIPE_INLET_MODULE)
    assert os.path.exists(Config.PIPE_TRANSFORMER_MODULE)
    assert os.path.exists(Config.PIPE_OUTLET_MODULE)
