from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from migrations.base_model import Base


class  User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str]
    role: Mapped[str]


