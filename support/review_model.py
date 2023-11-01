from sqlalchemy import Boolean, sql
from sqlalchemy.orm import Mapped, mapped_column

from migrations.base_model import Base


class Review(Base):
    __tablename__ = "reviews"

    topic: Mapped[str]
    message: Mapped[str]
    email: Mapped[str]
    name: Mapped[str]
    active: Mapped[bool]
    is_work: Mapped[bool] = mapped_column(Boolean, default=False, server_default=sql.false())
