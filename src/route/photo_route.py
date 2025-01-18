from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/photo",
    tags=["photo"],
)

@router.post(
    "/",
    description="사진을 업로드합니다."
)
def upload_photo():
    # TODO: need implementation
    return {"message": "Hello, World!"}
