from fastapi import Depends
from .. import schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import or_



#Method to insert the item in database

def create_item(request: schemas.Items, db: Session):
    new_item = models.Item(item_name=request.itemName, item_location=request.itemLocation,
     item_description=request.itemDescription, item_date=request.itemDate)

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


#Method to insert the item in database

def search_item(itemSearch: str, db: Session):
    item = db.query(models.Item).filter(
        or_(models.Item.item_name == itemSearch, models.Item.item_location == itemSearch)
    ).all()

    return item