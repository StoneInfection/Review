from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовая модель SqlAlchemy
    """

    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    # created_at: Mapped[datetime] = mapped_column(default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(
    #     TIMESTAMP(timezone=True),
    #     default=func.now(),
    #     onupdate=func.now()
    # )