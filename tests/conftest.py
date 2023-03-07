import os

os.environ["ENV"] = "test"
os.environ["SETUP"] = "no"

import shutil
import pytest
from time import sleep

from app.settings import SettingsManager
from app.settings.db import SQLBase
from app.repo_manager import RepoManager


def clear_settings(settings):
    settings.session.rollback()
    SQLBase.metadata.drop_all(settings.session.bind)
    settings.session.close()


@pytest.fixture
def settings():
    settings = SettingsManager("sqlite:///:memory:")
    yield settings
    clear_settings(settings)


@pytest.fixture
def default_settings():
    settings = SettingsManager("sqlite:///:memory:")
    settings.load_yaml("default-settings.yaml")
    yield settings
    clear_settings(settings)


@pytest.fixture
def test_settings():
    settings = SettingsManager("sqlite:///:memory:")
    settings.load_yaml("tests/test-settings.yaml")
    yield settings
    clear_settings(settings)


@pytest.fixture
def test_settings_and_repo():
    settings = SettingsManager("sqlite:///:memory:")
    settings.load_yaml("tests/test-settings.yaml")
    repo = RepoManager(settings)
    yield settings, repo
    clear_settings(settings)
