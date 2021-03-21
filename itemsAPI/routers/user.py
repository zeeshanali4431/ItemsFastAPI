from fastapi import APIRouter, Response, Depends
from .. import schemas, database
from ..crud import userCrud
from sqlalchemy.orm import Session

get_db = database.get_db


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model= schemas.UserShow)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userCrud.createUser(request, db)