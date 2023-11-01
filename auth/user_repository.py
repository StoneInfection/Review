from sqlalchemy import select
from sqlalchemy.orm import Session

from .user_model import User


class UserRepository:

    def create_user(self, db_session: Session, name: str, password: str, role: str):
        instance = User(name=name, password=password, role=role)
        db_session.add(instance)
        db_session.commit()
        db_session.refresh(instance)
        return instance

    def get_user(self, db_session: Session):
        stmt = select(User)
        raw = db_session.execute(stmt)
        return raw.scalars().first()
        # raw.scalar_one()

    def get_full_user(self, db_session: Session, pk: int):
        stmt = select(User).filter_by(id=pk)
        raw = db_session.execute(stmt)
        return raw.scalar_one()

    def get_user_by_name(self, db_session: Session, name: str):
        stmt = select(User).filter_by(name=name)
        raw = db_session.execute(stmt)
        return raw.scalar_one_or_none()

    def get_users_by_role(self, db_session: Session, role: str):
        stmt = select(User).filter_by(role=role)
        raw = db_session.execute(stmt)
        return raw.scalars().first()
