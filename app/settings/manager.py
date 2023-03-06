import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .db import SQLBase, Settings


class Setting:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"<Setting {self.name}={self.value}>"


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

    def set(self, setting_name: str, value: str, commit: bool = True) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting_name).first()
        if setting:
            setting.value = value
        else:
            setting = Settings(setting=setting_name, value=value)
        self.session.add(setting)
        if commit:
            self.session.commit()

    def all(self):
        return {
            setting.setting: setting.value
            for setting in self.session.query(Settings).all()
        }

    def list(self):
        return [setting.setting for setting in self.session.query(Settings).all()]

    def delete(self, setting: str, commit: bool = True) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            self.session.delete(setting)
            if commit:
                self.session.commit()
    
    def load_yaml(self, filename: str) -> None:
        with open(filename, "r") as f:
            loaded = yaml.load(f, Loader=yaml.FullLoader)
        self.load_dict(loaded)

    def load_dict(self, dictionary: dict[str, str]) -> None:
        for setting, value in dictionary.items():
            self.set(setting, value, commit=False)
        self.session.commit()

    def __getitem__(self, setting_name: str) -> str:
        setting = self.session.query(Settings).filter_by(setting=setting_name).first()
        if setting is None:
            raise KeyError(f"Setting {setting_name} not found")
        return setting.value
    
    def __iter__(self):
        return iter(self.all())
    
    def __dict__(self):
        return self.all()
    