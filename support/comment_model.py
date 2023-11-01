from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column


from migrations.base_model import Base


class Comment(Base):
    __tablename__ = 'comments'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    review_id: Mapped[int] = mapped_column(ForeignKey('reviews.id'))
    text: Mapped[str]
    # created_at: Mapped[datetime] = mapped_column(server_default=func.now)
