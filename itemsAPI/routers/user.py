from fastapi import APIRouter, Response
from .. import schemas
from ..crud import userCrud



router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model= schemas.UserShow)
def create_user(request: schemas.User):
    return userCrud.create(request)