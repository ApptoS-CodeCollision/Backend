from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from Routers import users, ais, chats, likes

# from DB import users, ais, chats, models, schemas, like
from DB import models
from DB.database import engine

from AI.crud import add_text, delete_text
from AI.main import rag_qa
from fastapi.middleware.cors import CORSMiddleware

from Blockchain import contract

import random
from time import ctime

# 데이터베이스 테이블 생성하기
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(ais.router, prefix="/ais", tags=["ais"])
app.include_router(chats.router, prefix="/chats", tags=["chats"])
app.include_router(likes.router, prefix="/likes", tags=["chats"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5000", 'https://apptos.ysblockblock.com'],  # 허용할 클라이언트의 도메인
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메서드 (GET, POST, OPTIONS 등)
    allow_headers=["*"],  # 허용할 헤더
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test/register_user", response_model=bool)
def get():
    contract.register_user(user_address="0xf8fc10130b2abd2562b02c6e05a64df1b8c802ff2c0820299c0a06b6bd6f63cd")
    return True

@app.get("/test/register_ai", response_model=bool)
def get():
    contract.register_ai(
        user_address="0xf8fc10130b2abd2562b02c6e05a64df1b8c802ff2c0820299c0a06b6bd6f63cd",
        creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",
        ai_id="ptwptw",
        rag_hash="0x123123123"
        )
    return True

@app.get("/test/store_embedding_data", response_model=bool)
def get():
    contract.store_embedding_data(
        user_address="0xf8fc10130b2abd2562b02c6e05a64df1b8c802ff2c0820299c0a06b6bd6f63cd",
        creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",
        ai_id="ptwptw",
        rag_hash="0x123123123"
        )
    return True

@app.get("/test/pay_for_usage", response_model=bool)
def get():
    contract.pay_for_usage(
        creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",
        ai_id="ptwptw",
        consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf",
        amount=50
        )
    return True

@app.get("/test/claim_rewards_by_ai", response_model=bool)
def get():
    contract.claim_rewards_by_ai(
        user_address="0xf8fc10130b2abd2562b02c6e05a64df1b8c802ff2c0820299c0a06b6bd6f63cd",
        creator_obj_address="0x32b0a3f384eab8bf44ad12121d4cfc04907b72dd8bb0c8bbf9147aa92e654e80",
        ai_id="ptwptw",
        )
    return True

@app.get("/test/recharge_consumer_balance_for_testing", response_model=bool)
def get():
    contract.recharge_consumer_balance_for_testing(
        consumer_obj_address="0x235c827ee71b580d8e2fb91f40a257e48c112d69dd8a1e63c365894998b7bfbf",
        )
    return True