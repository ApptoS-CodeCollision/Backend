from typing import List
from sqlalchemy.orm import Session

from DB import models
from Schema import base_schemas, user_schemas
from Blockchain import contract

def get_users(db: Session, offset: int, limit: int) -> List[models.UserTable]:
    return db.query(models.UserTable).offset(offset).limit(limit - offset).all()

def get_user(db: Session, user_address: str) -> user_schemas.UserRead:
    db_user =  db.query(models.UserTable).filter(models.UserTable.user_address == user_address).first()
    # SQLAlchemy ORM 객체를 Pydantic 모델로 변환
    user_dict = {column.name: getattr(db_user, column.name) for column in db_user.__table__.columns}
    trial = contract.view_get_free_trial_count(consumer_obj_address = db_user.consumer_obj_address)
    # base_schemas.User에 필요한 필드 전달
    user = user_schemas.UserRead(
        **user_dict,  # SQLAlchemy 객체 데이터를 언팩
        trial=trial  # 추가 필드
    )
    return user

def check_user_exists(db: Session, user_address: str) -> bool:
    return db.query(models.UserTable).filter(models.UserTable.user_address == user_address).first() is not None

def add_user(db: Session, user: base_schemas.User) -> models.UserTable:
    db_user_data = user.model_dump()

    # 모델 생성
    db_user = models.UserTable(**db_user_data)

    # 데이터베이스에 저장
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_update: user_schemas.UserUpdate) -> models.UserTable:
    db_user = db.query(models.UserTable).filter(models.UserTable.user_address == user_update.user_address).first()

    if db_user:
        for key, value in user_update.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

# def delete_user(db: Session, userid: str):
#     db_user = get_user(db, userid)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     return db_user
