from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/information",
    tags=["information"],
)

"""
# GET /information/@me

## request

## response

- tags: List<String>
- friends: List<String

"""

class InformationResponse(BaseModel):
    tags: List[str]
    friends: List[str]

@router.get(
    "/@me",
    description="내 정보를 조회합니다."
)
def get_my_information():
    # 예시 데이터
    return InformationResponse(
        tags=["희망", "우울", "행복", "슬픔", "화남", "화가남", "화가남", "화가남", "화가남", "화가남"],
        friends=["권민재", "이재은", "이수형", "오유림"]
    )
