from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session


class SQLBase_:
    id: Mapped[int] = mapped_column(primary_key=True)


SQLBase = declarative_base(cls=SQLBase_)


class Settings(SQLBase):
    __tablename__ = "settings"
    setting: Mapped[str] = mapped_column(unique=True)
    value: Mapped[Optional[str]] = mapped_column()


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

    def __getitem__(self, setting_name: str) -> str:
        setting = self.session.query(Settings).filter_by(setting=setting_name).first()
        if setting is None:
            raise KeyError(f"Setting {setting_name} not found")
        return setting.value
