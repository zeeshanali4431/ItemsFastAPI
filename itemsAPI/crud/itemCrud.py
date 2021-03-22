from fastapi import Depends
from .. import schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List



#Method to insert the item in database

def create_item(request: schemas.Items, db: Session):
    new_item = models.Item(item_name=request.item_name, item_location=request.item_location,
     item_description=request.item_description, item_date=request.item_date, user_id=1)

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item



#Method to get all the items from the database

def get_all_items(db: Session):
    item = db.query(models.Item).all()
    return item


#Method to Search the item from the database

def search_item(itemSearch: str, db: Session):
    item = db.query(models.Item).filter(
        or_(models.Item.item_name == itemSearch, models.Item.item_location == itemSearch)
    ).all()

    return item


#Method to delete the item from database

def delete_item(itemDelete: int, db: Session):
    item = db.query(models.Item).filter(models.Item.id == itemDelete)
    item.delete()
    db.commit()
    return 'Deleted...'


#Method to update the item from database

def update_item(id: int, request: schemas.Items, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id)
    item.update(request.dict())
    db.commit()
    return 'Updated..'