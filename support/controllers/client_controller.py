from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.services.auth_service import is_client
from auth.user_schema import UserSchema
from config.db_helper import db_helper
from support.support_schema import MessageResponse, MassageList, ActiveMessage

from ..services.client_servise import ReviewService


router = APIRouter(prefix="/support", tags=["client"])


@router.post("/", response_model=MessageResponse)
def add_message(
        data: ActiveMessage,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_client)
):
    return ReviewService().add(data, db_session)


@router.get("/{pk}", response_model=MessageResponse)
def get_message(
        pk: int,
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_client)
):
    return ReviewService().get(pk, db_session)


@router.get("/", response_model=list[MassageList])
def get_list_message(
        db_session: Session = Depends(db_helper.get_session),
        user: UserSchema = Depends(is_client)
):
    return ReviewService().get_lict(db_session)
