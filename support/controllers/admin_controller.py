from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session

from auth.services.auth_service import is_admin
from auth.user_schema import UserSchema
from config.db_helper import db_helper
from support.support_schema import MessageResponse, MassageList, UpdateMessage

from ..services.admin_service import ReviewService

router = APIRouter(prefix="/admin", tags=["admin"])


@router.put("/{pk}", response_model=MessageResponse)
def update_mess(
        pk: int,
        data: UpdateMessage,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return ReviewService().update(pk, data, db_session)


@router.delete("/{pk}")
def delete_message(
        pk: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    try:
        return ReviewService().delete(pk, db_session)
    except ValueError as e:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"{e}")


@router.get("/admin/{pk}", response_model=MessageResponse)
def get_message(
        pk: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return ReviewService().get(pk, db_session)


@router.get("/", response_model=list[MassageList])
def get_list_message(
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_admin)
):
    return ReviewService().get_lict(db_session)

