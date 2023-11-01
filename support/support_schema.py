from pydantic import BaseModel, EmailStr, ConfigDict, model_validator


class MessageBase(BaseModel):
    topic: str
    message: str
    name: str
    email: EmailStr


class CreateMessage(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int


class ActiveMessage(MessageBase):
    active: bool = False


class UpdateMessage(MessageBase):
    active: bool = False
    is_work: bool = False

    @model_validator(mode="after")
    def post_update(self):
        if self.active and self.is_work:
            raise ValueError("Нельзя делать оба True")
        return self


class UpdateMessageActive(BaseModel):
    active: bool = False


class MassageList(BaseModel):
    id: int
    topic: str
    name: str

