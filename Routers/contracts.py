from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from Blockchain import contract, legacy
from DB import utils

router = APIRouter()

@router.post("/register_user", response_model=bool)
def register_user(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    creator_obj_address, consumer_obj_addrsss = contract.register_user(user_address=user_address)
    # User Table에 creator_obj_address 와 consumer_obj_address 넣어 줘야 함




    return True

@router.post("/register_ai", response_model=str)
def register_ai(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    rag_hash: str = Query("", description="rag hash"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",




    tx_hash = contract.register_ai(
        user_address=user_address,
        creator_obj_address=creator_obj_address,
        ai_id=ai_id,
        rag_hash=rag_hash
    )
    return tx_hash

@router.post("/store_embedding_data", response_model=str)
def store_embedding_data(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    rag_hash: str = Query("", description="rag hash"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",




    tx_hash = contract.store_embedding_data(
        user_address=user_address,
        creator_obj_address=creator_obj_address,
        ai_id=ai_id,
        rag_hash=rag_hash
    )
    return tx_hash

@router.post("/pay_for_usage", response_model=str)
def pay_for_usage(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    amount: int = Query("", description="amount"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용(나중에 제거)
    # DB User table에서 검색해서 creator_obj_address, consumer_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf",




    tx_hash = contract.pay_for_usage(
        creator_obj_address=creator_obj_address,
        ai_id=ai_id,
        consumer_obj_address=consumer_obj_address,
        amount=amount
    )
    return tx_hash

@router.post("/claim_rewards_by_ai", response_model=str)
def claim_rewards_by_ai(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",





    tx_hash = contract.claim_rewards_by_ai(
        user_address=user_address,
        creator_obj_address=creator_obj_address,
        ai_id="ptwptw",
    )
    return tx_hash

@router.post("/request_faucet", response_model=str)
def request_faucet(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 consumer_obj_address (나중에 제거)
    # DB User table에서 검색해서 consumer_obj_address 가져와서 사용
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"





    tx_hash = contract.request_faucet(
        consumer_obj_address=consumer_obj_address,
    )
    return tx_hash

@router.post("/use_free_trial", response_model=str)
def use_free_trial(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 consumer_obj_address (나중에 제거)
    # DB User table에서 검색해서 consumer_obj_address 가져와서 사용
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"





    tx_hash = contract.use_free_trial(
        consumer_obj_address=consumer_obj_address,
    )
    return tx_hash

@router.post("/test/recharge_consumer_balance_for_testing", response_model=str)
def recharge_consumer_balance_for_testing():
    tx_hash = legacy.recharge_consumer_balance_for_testing(
        consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf",
        )
    return tx_hash


@router.get("/exists_creator_at", response_model=str)
def view_exists_creator_at(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80"

    return contract.view_exists_creator_at(creator_obj_address=creator_obj_address)

@router.get("/exists_consumer_at", response_model=str)
def view_exists_consumer_at(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 consumer_obj_address (나중에 제거)
    # DB User table에서 검색해서 consumer_obj_address 가져와서 사용
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"

    return contract.view_exists_consumer_at(consumer_obj_address=consumer_obj_address)

@router.get("/contain_ai", response_model=str)
def view_contain_ai(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80"

    return contract.view_contain_ai(creator_obj_address=creator_obj_address, ai_id=ai_id)

@router.get("/ai_rewards", response_model=str)
def view_get_ai_rewards(
    user_address: str = Query("", description="user address"),
    ai_id: str = Query("", description="ai id"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 creator_obj_address (나중에 제거)
    # DB User table에서 검색해서 creator_obj_address 가져와서 사용
    creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80"

    return contract.view_get_ai_rewards(creator_obj_address=creator_obj_address, ai_id=ai_id)

@router.get("/consumer_balance", response_model=str)
def view_get_consumer_balance(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 consumer_obj_address (나중에 제거)
    # DB User table에서 검색해서 consumer_obj_address 가져와서 사용
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"

    return contract.view_get_consumer_balance(consumer_obj_address=consumer_obj_address)

@router.get("/free_trial_count", response_model=str)
def view_get_free_trial_count(
    user_address: str = Query("", description="user address"),
    db: Session = Depends(utils.get_db)
):
    # 임시 용 consumer_obj_address (나중에 제거)
    # DB User table에서 검색해서 consumer_obj_address 가져와서 사용
    consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf"

    return contract.view_get_free_trial_count(consumer_obj_address=consumer_obj_address)

