from fastapi import Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
import re


#Method to create the user in database

def createUser(request: schemas.User, db: Session):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    pat = re.compile(reg)
    mat = re.search(pat, request.password)
    if mat:
        new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
         detail="password must be atlest 8 characters log and have atleast one upper and one lower and one special character")
    return new_user


    