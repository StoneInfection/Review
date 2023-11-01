from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session

from auth.services.auth_service import is_manager
from auth.user_schema import UserSchema
from config.db_helper import db_helper
from support.support_schema import MessageResponse, MassageList, UpdateMessage, UpdateMessageActive

from ..services.manager_servise import ReviewService


router = APIRouter(prefix="/manager", tags=["manager"])


@router.put("/{pk}", response_model=MessageResponse)
def update_mess(
        pk: int,
        data: UpdateMessage,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_manager)
):
    return ReviewService().update(pk, data, db_session)


@router.patch("/{pk}", response_model=MessageResponse)
def update_active(
        pk: int,
        data: UpdateMessageActive,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_manager)
):
    try:
        return ReviewService().update_act(pk, data, db_session)
    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"{e}")


@router.get("/manager/{pk}", response_model=MessageResponse)
def get_message(
        pk: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_manager)
):
    return ReviewService().get(pk, db_session)


@router.get("/", response_model=list[MassageList])
def get_list_message(
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_manager)
):
    return ReviewService().get_lict(db_session)
