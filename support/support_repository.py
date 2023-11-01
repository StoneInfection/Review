from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from support.support_schema import UpdateMessage, ActiveMessage, UpdateMessageActive
from support.review_model import Review


class SupportRepository:

    def create_message(self, db_session: Session, data: ActiveMessage):
        instance = Review(**data.model_dump())
        db_session.add(instance)
        db_session.commit()
        db_session.refresh(instance)
        return instance

    def update_message(self, db_session: Session, data: UpdateMessage, pk: int):
        stmt = update(Review).values(**data.model_dump()).filter_by(id=pk).returning(Review)
        raw = db_session.execute(stmt)
        db_session.commit()
        return raw.scalar_one()

    def update_message_active(self, db_session: Session, data: UpdateMessageActive, pk: int):
        stmt = update(Review).values(**data.model_dump()).filter_by(id=pk).returning(Review)
        raw = db_session.execute(stmt)
        db_session.commit()
        return raw.scalar_one()

    def delete_message(self, db_session: Session, pk: int) -> None:
        stmt = delete(Review).where(Review.id == pk)
        db_session.execute(stmt)
        db_session.commit()

    def get_massages(self, db_session: Session):
        stmt = select(Review)
        raw = db_session.execute(stmt)
        return raw.scalars()
        # raw.scalar_one()

    def get_full_message(self, db_session: Session, pk: int):
        stmt = select(Review).filter_by(id=pk)
        raw = db_session.execute(stmt)
        return raw.scalar_one()
