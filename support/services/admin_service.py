from sqlalchemy.orm import Session

from support.support_repository import SupportRepository
from support.support_schema import UpdateMessage


class ReviewService:

    def __init__(self):
        self.repository = SupportRepository()

    def update(self, pk: int, data: UpdateMessage, db_session: Session):
        return self.repository.update_message(db_session, data, pk)

    def delete(self, pk: int, db_session: Session):
        mess = self.repository.get_full_message(db_session, pk)
        if mess.is_work:
            raise ValueError("Нельзя удалить так как находится в работе")
        self.repository.delete_message(db_session, pk)

    def get(self, pk: int, db_session: Session):
        return self.repository.get_full_message(db_session, pk)

    def get_lict(self, db_session: Session):
        return self.repository.get_massages(db_session)
