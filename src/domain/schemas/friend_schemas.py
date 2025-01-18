from pydantic import BaseModel, ConfigDict


class FriendWithStatisticResponse(BaseModel):
    id: int
    name: str
    image: str | None
    totalCount: int
    localCount: int
    ratio: float

    class Config:
        from_attributes = True  # SQLAlchemy 모델을 Pydantic 모델로 변환 허용
