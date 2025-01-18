from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/friend",
    tags=["friend"],
)

class FriendWithStatisticResponse(BaseModel):
    id: int
    name: str
    image: str
    totalCount: int
    localCount: int
    ratio: float


@router.get("/friend/with-statistic", response_model=List[FriendWithStatisticResponse])
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
            "image": "https://mblogthumb-phinf.pstatic.net/20091005_167/tsuki924_1254712963371ULps1_jpg/%C1%B6%B7%CE_tsuki924.jpg",
            "totalCount": 50,
            "localCount": 45,
            "ratio": 0.9
        }
    ]

    # ratio를 기준으로 내림차순 정렬
    sorted_friends = sorted(
        friends_data, key=lambda x: x["ratio"], reverse=True)
    return sorted_friends
