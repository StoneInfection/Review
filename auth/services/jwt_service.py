import jwt
from datetime import datetime, timedelta

from config.project_config import settings


class JwtService:
    ALGORITHM = "HS256"
    access_token_jwt_subject = "access"

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXP)
        to_encode.update({"exp": expire, "sub": self.access_token_jwt_subject})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
