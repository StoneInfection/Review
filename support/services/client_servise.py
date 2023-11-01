from sqlalchemy.orm import Session

from support.support_repository import SupportRepository
from support.support_schema import ActiveMessage


class ReviewService:

    def __init__(self):
        self.repository = SupportRepository()

    def add(self, data: ActiveMessage, db_session: Session):
        return self.repository.create_message(db_session, data)

    def get(self, pk: int, db_session: Session):
        return self.repository.get_full_message(db_session, pk)

    def get_lict(self, db_session: Session):
        return self.repository.get_massages(db_session)
