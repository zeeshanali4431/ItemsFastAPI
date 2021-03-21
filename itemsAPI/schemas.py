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
    item_name: str
    item_location: str
    item_description: str
    item_date : date
