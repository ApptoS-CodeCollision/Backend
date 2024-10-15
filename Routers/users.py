from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from DB import utils, users
from Schema import base_schemas, user_schemas
from Blockchain import contract


router = APIRouter()

@router.get("/", response_model=base_schemas.UserList)
def get_users(
    offset: int = Query(0, description="Offset for pagination"), 
    limit: int = Query(10, description="Limit for pagination"), 
    db: Session = Depends(utils.get_db)
):
    res = users.get_users(db=db, offset=offset, limit=limit)
    return base_schemas.UserList(users=res)

@router.get("/{user_address}", response_model=base_schemas.User)
def get_user(user_address : str, db: Session = Depends(utils.get_db)):
    check_user = users.check_user_exists(db=db, user_address=user_address)
    if not check_user:
        raise HTTPException(status_code=400, detail="User Doesn't Exist")
    return users.get_user(db, user_address=user_address)

@router.get("/exists/{user_address}", response_model=bool)
def check_user_exists(user_address : str, db: Session = Depends(utils.get_db)):
    return users.check_user_exists(db = db, user_address=user_address)

@router.post("/", response_model=base_schemas.User)
def add_user(user: user_schemas.UserCreate, db: Session = Depends(utils.get_db)):
    check_user = users.check_user_exists(db=db, user_address=user.user_address)
    if check_user:
        raise HTTPException(status_code=400, detail="User Already Exists")

    return users.add_user(db, user=user)


@router.post("/faucet/{user_address}", response_model=str)
def charge_user(user_address: str, db: Session = Depends(utils.get_db)):
    ########### BlockChain에 충전하기 위한 로직 #################
    # 사용자의 정보를 가져오기
    user_info = users.get_user(db=db, user_address=user_address)
    
    # 사용자가 존재하지 않으면 예외 발생
    if not user_info:
        raise HTTPException(status_code=400, detail="User Doesn't Exist")
    try:
        tx_hash = contract.request_faucet(user_address=user_info.user_address)
        return tx_hash  # 성공 시 True 반환
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update user: " + str(e))


@router.put("/", response_model=base_schemas.User)
def update_user(user: user_schemas.UserUpdate, db: Session = Depends(utils.get_db)):
    check_user = users.check_user_exists(db=db, user_address=user.user_address)
    if not check_user:
        raise HTTPException(status_code=400, detail="User Doesn't Exists")
    return users.update_user(db, user_update = user)
