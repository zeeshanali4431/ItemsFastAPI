from fastapi import FastAPI, APIRouter, Depends
from .. import schemas, database, models
from ..crud import itemCrud
from sqlalchemy.orm import Session



get_db = database.get_db


router= APIRouter(
    prefix='/item',
    tags=['Items']
)



#Route for the insert item in database

@router.post('/')
def createItem(request: schemas.Items, db: Session=Depends(get_db)):
    return itemCrud.create_item(request, db)


#Route for the insert item in database

@router.get('/')
def searchItem(item: str, db: Session=Depends(get_db)):
    return itemCrud.search_item(item, db)