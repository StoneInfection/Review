from sqlalchemy import select
from sqlalchemy.orm import Session

from support.comment_model import Comment
from comment_schema import CreateCommentSchema


class CommentRepository:

    def add_comment(self, db_session: Session, data: CreateCommentSchema, user_id: int):
        instance = Comment(**data.model_dump(), user_id=user_id)
        db_session.add(instance)
        db_session.commit()
        db_session.refresh(instance)
        return instance

    def get_full_comment(self, db_session: Session):
        stmt = select(Comment)
        raw = db_session.execute(stmt)
        return raw.scalars()
        # raw.scalar_one()

    def get_comment_user_id(self, db_session: Session, user_id: int):
        stmt = select(Comment).filter_by(user_id=user_id)
        raw = db_session.execute(stmt)
        return raw.scalars()

    def get_comment_review_id(self, db_session: Session, review_id: int):
        stmt = select(Comment).filter_by(review_id=review_id)
        raw = db_session.execute(stmt)
        return raw.scalars()
# def add_comments(db_session: Session, data: CreateCommentSchema, pk: int):
#     stmt = update(Comment).values(**data.model_dump()).filter_by(id=pk).returning(Comment)
#     raw = db_session.execute(stmt)
#     db_session.commit()
#     return raw.scalar_one() 
#           raw.scalars().first()

