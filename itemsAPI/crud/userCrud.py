from fastapi import Depends
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash


#Method to create the user in database

def createUser(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user