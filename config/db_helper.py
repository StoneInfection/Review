from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)
from sqlalchemy.orm import sessionmaker

from .db_config import settings_db


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        # self.engine = create_async_engine(url=url, echo=echo)
        #
        # self.session_factory = async_sessionmaker(
        #     bind=self.engine,
        #     autoflush=False,
        #     autocommit=False,
        #     expire_on_commit=False
        # )

        engine = create_engine(url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_session(self):
        from sqlalchemy import exc

        session = self.SessionLocal()
        try:
            yield session
        except exc.SQLAlchemyError as error:
            session.rollback()
            raise
        finally:
            session.close()

    # @asynccontextmanager
    # async def get_db_session(self):
    #     from sqlalchemy import exc
    #
    #     session: AsyncSession = self.session_factory()
    #     try:
    #         yield session
    #     except exc.SQLAlchemyError as error:
    #         await session.rollback()
    #         raise
    #     finally:
    #         await session.close()


db_helper = DatabaseHelper(settings_db.database_url, settings_db.DB_ECHO_LOG)


# db: Session = Depends(db_helper.get_session)