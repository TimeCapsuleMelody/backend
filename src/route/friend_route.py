from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field

from domain.schemas.friend_schemas import FriendWithStatisticResponse

router = APIRouter(
    prefix="/friend",
    tags=["friend"],
)


@router.get(
    "/with-statistic",
    response_model=List[FriendWithStatisticResponse],
    description="친구 목록을 통계 정보와 함께 조회합니다."
)
def get_friends_with_statistic():
    # 예시 데이터
    friends_data = [
        {
            "id": 1,
            "name": "루피",
            "image": "https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg",
            "totalCount": 100,
            "localCount": 80,
            "ratio": 0.8
        },
        {
            "id": 2,
            "name": "조로",
            "image": "https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg",
            "totalCount": 50,
            "localCount": 45,
            "ratio": 0.9
        }
    ]

    # ratio를 기준으로 내림차순 정렬
    sorted_friends = sorted(
        friends_data, key=lambda x: x["ratio"], reverse=True)
    return sorted_friends
