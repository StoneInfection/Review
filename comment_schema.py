from pydantic import BaseModel


class CommentBase(BaseModel):
    id: int
    user_id: int
    review_id: int
    text: str
    # data: str


class CreateCommentSchema(BaseModel):
    text: str
    review_id: int


class CommentResponse(CommentBase):
    pass
