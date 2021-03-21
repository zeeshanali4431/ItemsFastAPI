from fastapi import FastAPI
from .routers import user, item
from . import models
from .database import engine




app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(item.router)