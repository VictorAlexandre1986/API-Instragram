from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from db.models import DbUser
from sqlalchemy.orm import Session
from db.hashing import Hash
from auth.oauth2 import create_access_token
from db.config import get_db
from fastapi import APIRouter

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    # if not Hash.verify(user.password, request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    access_token = create_access_token(data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer", "user": user.username}
