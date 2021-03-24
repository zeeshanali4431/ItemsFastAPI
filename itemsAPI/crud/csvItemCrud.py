from fastapi import Depends
from sqlalchemy.orm import Session
from .. import models
import csv
import codecs




#method to process the bulk records for items

def csv_process_items(myFile, db:Session):
    csv_reader = csv.reader(codecs.iterdecode(myFile.file,'utf-8'))

    for line in csv_reader:
        new_item = models.Item(item_name=line[0], item_location=line[1],
         item_description=line[2], item_date=line[3], user_id=line[4])

        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    return 'Done..'
