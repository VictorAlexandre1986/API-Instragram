from fastapi import APIRouter,Depends,status,File
from fastapi.exceptions import HTTPException
from fastapi.datastructures import UploadFile
from sqlalchemy.orm import Session
from schema.schema import PostBase,PostDisplay  
from db.config import get_db
from db import db_post
from typing import List
import random
import string
import shutil
from schema.schema import UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/post',
    tags=['post']
)

#Tem que passsar absolute ou relatve no campo image_url_type do swagger
image_url_types = ['absolute', 'relative']

@router.post('', response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Parameter image_url_type can only take values  "absolute", or "relative"')
    return db_post.create(db, request)  


@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.post('/image')
def upload_image(image: UploadFile = File(...),  current_user: UserAuth = Depends(get_current_user)):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_name = [random.choice(letters) for i in range(10)]
    random_name = ''.join(random_name)
    file_name = f'_{random_name}.'
    # file_name = new.join(image.filename.rsplit('.', 1))
    path = f'images/{file_name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"filename": path}

@router.get('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete_post(db, id, current_user.id)
