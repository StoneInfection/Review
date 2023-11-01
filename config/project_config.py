from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv('.env')


class ProjectConfig(BaseSettings):
    SECRET_KEY: str
    JWT_EXP: int


settings = ProjectConfig()
