from fastapi import APIRouter, Response, Depends
from .. import schemas, database, models, oauth2
from ..crud import itemCrud
from sqlalchemy.orm import Session
from typing import List



get_db = database.get_db


router= APIRouter(
    prefix='/item',
    tags=['Items']
)



#Route for the insert item in database

@router.post('/', response_model=schemas.Items)
def createItem(request: schemas.Items, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return itemCrud.create_item(request, db)


#Route for the insert item in database

@router.get('/', response_model=List[schemas.ShowItems])
def searchItem(item: str, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return itemCrud.search_item(item, db)


#Route for the list of all items in database

@router.get('/all', response_model=List[schemas.ShowItems])
def getAllItem(db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return itemCrud.get_all_items(db)


#Route for the delete item in database

@router.delete('/{id}')
def deleteItem(id: int, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return itemCrud.delete_item(id, db)


#Route for the update item in database

@router.put('/update')
def updateItem(id: int, request: schemas.Items, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return itemCrud.update_item(id, request, db)