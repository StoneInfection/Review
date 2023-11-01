from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from config.db_helper import db_helper

from auth.services.user_servise import UserService
from .user_schema import UserSchema,  UserRegistration

router = APIRouter(prefix="/user", tags=["user"])


@router.post('/registration', response_model=UserSchema)
def registration(user: UserRegistration, db_session: Session = Depends(db_helper.get_session)):
    try:
        print(user)
        return UserService().add(user.name, user.password, "user", db_session)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# @router.post("/", response_model=UserSchema)
# def add_message(
#         data: UserCreate,
#         db_session: Session = Depends(db_helper.get_session),
# ):
#     return ReviewService().add(data, db_session)
#
#
# @router.get("/{pk}", response_model=UserSchema)
# def get_message(
#         pk: int,
#         db_session: Session = Depends(db_helper.get_session)
# ):
#     return ReviewService().get(pk, db_session)
#
#
# @router.get("/", response_model=list[UserSchema])
# def get_list_message(
#         db_session: Session = Depends(db_helper.get_session),
# ):
#     return ReviewService().get_lict(db_session)
