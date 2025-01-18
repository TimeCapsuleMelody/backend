from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Music(BaseModel):
    musicId: int
    musicTitle: str
    date: str
    friends: List[str]
    diary: str
    feeling: int
    keywords: List[str]
    image: str

    model_config = ConfigDict(from_attributes=True)


class MusicByPeriod(BaseModel):
    year: int
    month: int
    music: List[Music]

    model_config = ConfigDict(from_attributes=True)


class SearchMusicResponse(BaseModel):
    title: str
    thumbnail: str
    url: str

    model_config = ConfigDict(from_attributes=True)
