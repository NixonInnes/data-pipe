from typing import Optional
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


class SQLBase_:
    id: Mapped[int] = mapped_column(primary_key=True)


SQLBase = declarative_base(cls=SQLBase_)


class Settings(SQLBase):
    __tablename__ = "settings"
    setting: Mapped[str] = mapped_column(unique=True)
    value: Mapped[Optional[str]] = mapped_column()
