from typing import List

from pydantic import BaseModel, ConfigDict


class FriendResponse(BaseModel):
    id: int
    name: str
    photo: str

    model_config = ConfigDict(from_attributes=True)


class KeywordResponse(BaseModel):
    id: int
    keyword: str

    model_config = ConfigDict(from_attributes=True)


class InformationResponse(BaseModel):
    tags: List[KeywordResponse]
    friends: List[FriendResponse]

    model_config = ConfigDict(from_attributes=True)
