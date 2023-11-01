from fastapi import FastAPI
from support.controllers import admin_controller, client_controller, manager_controller
import  comment_controller
from auth import user_controller

app = FastAPI()


app.include_router(admin_controller.router)
app.include_router(manager_controller.router)
app.include_router(client_controller.router)
app.include_router(user_controller.router)
app.include_router(comment_controller.router)
