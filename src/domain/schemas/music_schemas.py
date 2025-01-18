from typing import List, Optional

from pydantic import BaseModel, Field


class Music(BaseModel):
    musicId: int
    musicTitle: str
    date: str
    friend: str
    diary: str
    feeling: int
    keywords: List[str]
    image: str


class MusicByPeriod(BaseModel):
    year: int
    month: int
    music: List[Music]


class SearchMusicResponse(BaseModel):
    title: str
    thumbnail: str
    url: str
