from pydantic import BaseModel


class FriendWithStatisticResponse(BaseModel):
    id: int
    name: str
    image: str
    totalCount: int
    localCount: int
    ratio: float
