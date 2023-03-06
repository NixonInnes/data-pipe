import pytest

from app.settings import SettingsManager
from app.settings.db import SQLBase


@pytest.fixture
def settings():
    settings = SettingsManager("sqlite:///:memory:")
    yield settings
    settings.session.rollback()
    SQLBase.metadata.drop_all(settings.session.bind)
    settings.session.close()
