from sqlalchemy.orm import Session

from comment_repository import CommentRepository
from comment_schema import CreateCommentSchema


class CommService:

    def __init__(self):
        self.repository = CommentRepository()

    def comm_add(self, user_id: int, data: CreateCommentSchema, db_session: Session):
        return self.repository.add_comment(db_session, data, user_id)

    def get_full(self, db_session: Session):
        return self.repository.get_full_comment(db_session)

    def get_user_id(self, user_id: int, db_session: Session):
        return self.repository.get_comment_user_id(db_session, user_id)

    def get_review_id(self, review_id: int, db_session: Session):
        return self.repository.get_comment_review_id(db_session, review_id)
