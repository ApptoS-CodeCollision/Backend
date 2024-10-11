from pydantic import BaseModel
from typing import List, Optional
from datetime import time, datetime
from Schema import base_schemas

class UserUpdate(BaseModel):
    user_address: str
    nickname: str = '0.0'
    gender: str
    country: str
    interest: str
    profile_image_url: str


class UserCreate(BaseModel):
    user_address: str
    nickname: str = '0.0'
    gender: str
    country: str
    interest: str
    profile_image_url: str
