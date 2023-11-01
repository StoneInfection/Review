from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from auth.user_repository import UserRepository
from auth.user_schema import UserSchema
from config.db_helper import db_helper


oauth2_scheme = APIKeyHeader(name="role")


class AuthService:
    def __init__(self, role: str):
        self.role = role

    def __call__(self, role: str = Depends(oauth2_scheme), db_session: Session = Depends(db_helper.get_session)):
        if self.role == role:
            user = UserRepository().get_users_by_role(db_session=db_session, role=role)
            if user is not None:
                return UserSchema.model_validate(user, from_attributes=True)
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


is_admin = AuthService("admin")
is_client = AuthService("client")
is_manager = AuthService("manager")


# user_sql = repo()
# UserSchema(name=user_sql.name, role=user_sql.role, id=user_sql.id)
# UserSchema.model_validate(user_sql)

