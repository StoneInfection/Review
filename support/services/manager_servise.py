from sqlalchemy.orm import Session

from support.support_repository import SupportRepository
from support.support_schema import UpdateMessage, UpdateMessageActive


class ReviewService:

    def __init__(self):
        self.repository = SupportRepository()

    def update(self, pk: int, data: UpdateMessage, db_session: Session):
        return self.repository.update_message(db_session, data, pk)

    def update_act(self, pk: int, data: UpdateMessageActive, db_session: Session):
        mess = self.repository.get_full_message(db_session, pk)
        if mess.is_work and data.active:
            raise ValueError("Нельзя active true так как находится в работе")
        return self.repository.update_message_active(db_session, data, pk)

    def get(self, pk: int, db_session: Session):
        return self.repository.get_full_message(db_session, pk)

    def get_lict(self, db_session: Session):
        return self.repository.get_massages(db_session)