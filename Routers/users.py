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
def add_user(user: base_schemas.User, db: Session = Depends(utils.get_db)):
    check_user = users.check_user_exists(db=db, user_address=user.user_address)
    if check_user:
        raise HTTPException(status_code=400, detail="User Already Exists")
    
    ########### BlockChain에 유저 정보 저장 불필요? #################

    ##### TODO : User Table에 creator_obj_address 와 consumer_obj_address 넣어 줘야 함
    creator_obj_address, consumer_obj_addrsss = contract.register_user(user_address=user.user_address)


    return users.add_user(db, user = user)


@router.post("/charge/{user_address}", response_model=bool)
def charge_user(user_address: str, db: Session = Depends(utils.get_db)):
    ########### BlockChain에 충전하기 위한 로직 #################
    # 여기에 블록체인 충전 로직을 추가하세요.

    ##### TODO : DB User table user_address 검색해서 consumer_obj_address 가져와서 사용
    
    ##### 임시 용 consumer_obj_address (나중에 제거)
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"

    tx_hash = contract.request_faucet(
        consumer_obj_address=consumer_obj_address,
    )

    ##### Test ######
    # 사용자의 정보를 가져오기
    user_info = users.get_user(db=db, user_address=user_address)
    
    # 사용자가 존재하지 않으면 예외 발생
    if not user_info:
        raise HTTPException(status_code=400, detail="User Doesn't Exist")
    
    # 사용자의 trial 값을 업데이트
    user_info.trial = 10
    
    # DB에 변경 사항 반영
    try:
        db.commit()  # DB 세션에 커밋하여 업데이트 반영
        db.refresh(user_info)  # 최신 데이터를 다시 가져옴
        return True  # 성공 시 True 반환
    except Exception as e:
        db.rollback()  # 오류 발생 시 롤백
        raise HTTPException(status_code=500, detail="Failed to update user: " + str(e))


@router.put("/", response_model=base_schemas.User)
def update_user(user: user_schemas.UserUpdate, db: Session = Depends(utils.get_db)):
    check_user = users.check_user_exists(db=db, user_address=user.user_address)
    if not check_user:
        raise HTTPException(status_code=400, detail="User Doesn't Exists")
    return users.update_user(db, user_update = user)
