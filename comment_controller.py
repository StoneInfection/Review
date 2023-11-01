from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.services.auth_service import is_admin
from auth.user_schema import UserSchema
from comment_service import CommService
from config.db_helper import db_helper
from comment_schema import CreateCommentSchema, CommentResponse


router = APIRouter(prefix="/comment", tags=["comment"])


@router.post("/", response_model=CommentResponse)
def add_comment(
    data: CreateCommentSchema,
    db_session: Session = Depends(db_helper.get_session),
    user: UserSchema = Depends(is_admin)
):
    return CommService().comm_add(user_id=user.id, data=data, db_session=db_session)


@router.get("/", response_model=list[CommentResponse])
def get_comment(
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return CommService().get_full(db_session)


@router.get("/admin/{user_id}", response_model=list[CommentResponse])
def get_list_comment_user_id(
        user_id: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return CommService().get_user_id(user_id=user_id, db_session=db_session)


@router.get("/admin/review/{review_id}", response_model=list[CommentResponse])
def get_list_comment_review_id(
        review_id: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return CommService().get_review_id(review_id=review_id, db_session=db_session)
