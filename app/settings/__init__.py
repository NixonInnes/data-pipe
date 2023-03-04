from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session


class SQLBase_:
    id: Mapped[int] = mapped_column(primary_key=True)

SQLBase = declarative_base(cls=SQLBase_)

class Settings(SQLBase):
    __tablename__ = 'settings'
    setting: Mapped[str] = mapped_column(unique=True)
    value: Mapped[Optional[str]] = mapped_column()


class SettingsManager:
    def __init__(self, db_uri: str):
        engine = create_engine(db_uri, echo=True)
        SQLBase.metadata.create_all(engine)
        self.session = Session(engine)
    
    def get(self, setting: str, default: str|None = None) -> Optional[str]:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            return setting.value
        return default
    
    def set(self, setting: str, value: str) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            setting.value = value
        else:
            setting = Settings(setting=setting, value=value)
            self.session.add(setting)
        self.session.commit()
    
    def delete(self, setting: str) -> None:
        setting = self.session.query(Settings).filter_by(setting=setting).first()
        if setting:
            self.session.delete(setting)
            self.session.commit()

