from pydantic import BaseModel



class User(BaseModel):
    name: str
    email: str
    password: str

class UserShow(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True