from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from db.config import get_db
from db import db_comment
from schema.schema import CommentBase, UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create(db, request)

@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)

@router.get('/delete/{id}')
def delete_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.delete_comment(db, id)
