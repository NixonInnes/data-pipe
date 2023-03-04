import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .db import SQLBase, Settings


class SettingsManager:
    def __init__(self, db_uri: str):
        engine = create_engine(db_uri)
        SQLBase.metadata.create_all(engine)
        self.session = Session(engine)

    def get(self, setting: str, default: str | None = None) -> str | None:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            return setting.value
        return default

    def set(self, setting_name: str, value: str) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting_name).first()
        if setting:
            setting.value = value
        else:
            setting = Settings(setting=setting_name, value=value)
            self.session.add(setting)
        self.session.commit()

    def all(self):
        return {
            setting.setting: setting.value
            for setting in self.session.query(Settings).all()
        }

    def list(self):
        return [setting.setting for setting in self.session.query(Settings).all()]

    def delete(self, setting: str) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            self.session.delete(setting)
            self.session.commit()
    
    def load_yaml(self, filename):
        with open(filename, "r") as f:
            loaded = yaml.load(f, Loader=yaml.FullLoader)
        for setting, value in loaded.items():
            self.set(setting, value)

    def __getitem__(self, setting_name: str) -> str:
        setting = self.session.query(Settings).filter_by(setting=setting_name).first()
        if setting is None:
            raise KeyError(f"Setting {setting_name} not found")
        return setting.value