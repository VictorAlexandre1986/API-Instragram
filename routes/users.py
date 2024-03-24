from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schema.schema import UserBase,UserDisplay
from db.config import get_db
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('',response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
    