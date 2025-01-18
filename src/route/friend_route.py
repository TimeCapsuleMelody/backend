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
            "image": "https://private-user-images.githubusercontent.com/75142329/404548451-be01b7e3-4319-4708-bb59-218e4751c80b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcyMTg5NDcsIm5iZiI6MTczNzIxODY0NywicGF0aCI6Ii83NTE0MjMyOS80MDQ1NDg0NTEtYmUwMWI3ZTMtNDMxOS00NzA4LWJiNTktMjE4ZTQ3NTFjODBiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTE4VDE2NDQwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJhMDMxYzQzOWEzZjg0ZmRlMzQ5NWNjMzIzYjQ0ODAxYTg1MDc0NWY1MmJjZTU2YTM1ZTI2ZmZhZmUwZDUyNjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.DQ3JElEJbLXp-3iGS_Y8TXdyH9sWfMMoQ1GanM2Pw1s",
            "totalCount": 50,
            "localCount": 45,
            "ratio": 0.9
        }
    ]

    # ratio를 기준으로 내림차순 정렬
    sorted_friends = sorted(
        friends_data, key=lambda x: x["ratio"], reverse=True)
    return sorted_friends
