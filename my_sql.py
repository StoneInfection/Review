from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload
from support.review_model import Review


# stmt = select(Review.id).where(Review.id==2)

stmt = insert(Review).values({"id": 2})
print(stmt)