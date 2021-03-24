from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..hashing import Hash
import csv
import codecs
import re





#method to process the bulk records for users

def csv_process_users(myFile, db:Session):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    pat = re.compile(reg)

    csv_reader = csv.reader(codecs.iterdecode(myFile.file,'utf-8'))

    for line in csv_reader:
        
        mat = re.search(pat, line[2])

        if mat:
            new_user = models.User(name=line[0], email=line[1], password=Hash.bcrypt(line[2]))
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
             detail="password must be atlest 8 characters log and have atleast one upper and one lower and one special character")

    return 'Done..'