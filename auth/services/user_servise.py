from sqlalchemy.orm import Session

from ..user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def add(self, name: str, password: str, role: str, db_session: Session):
        if self.repository.get_user_by_name(db_session, name):
            raise Exception("User already exists")
        return self.repository.create_user(db_session, name, password, role)

    def get(self, pk: int, db_session: Session):
        return self.repository.get_full_user(db_session, pk)

    def get_lict(self, db_session: Session):
        return self.repository.get_user(db_session)
