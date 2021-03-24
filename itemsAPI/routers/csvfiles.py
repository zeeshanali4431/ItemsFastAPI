from fastapi import APIRouter, Depends, File, UploadFile
from ..crud import csvItemCrud, csvUserCrud
from .. import database
from sqlalchemy.orm import Session



get_db = database.get_db

router = APIRouter(tags=['CSVs'])



@router.post('/csvitems')
def get_csvfile(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return csvItemCrud.csv_process_items(file, db)


@router.post('/csvusers')
def get_csvfile(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return csvUserCrud.csv_process_users(file, db)