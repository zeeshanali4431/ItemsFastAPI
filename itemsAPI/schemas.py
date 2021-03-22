from pydantic import BaseModel
from typing import Optional
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
    
    class Config():
        orm_mode = True


#Response model for showing the Relationship b/w User and Items

class ShowItems(BaseModel):
    item_name: str
    item_location: str
    item_description: str
    item_date : date

    user : UserShow
    class Config():
        orm_mode = True


#Schema for the Login

class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None