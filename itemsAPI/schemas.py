from pydantic import BaseModel
from datetime import date





""" schema for User model will be used in userCrud"""

class User(BaseModel):
    name: str
    email: str
    password: str

#Response model for showing the specific attributes to the user

class UserShow(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


""" schema for item model will be used in itemCrud"""

class Items(BaseModel):
    itemName: str
    itemLocation: str
    itemDescription: str
    itemDate : date
