from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field

from dependencies import get_db
from domain.schemas.music_schemas import Music

router = APIRouter(
    prefix="/memory",
    tags=["memory"],
)


@router.post(
    "/",
    description="Music(추억)을 저장합니다."
)
async def save_music(music: Music):
    # return 200 OK
    return {"message": "Music saved successfully"}
