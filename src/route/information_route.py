from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field

from repository.models import Keyword, Friend

from dependencies import get_db
from domain.schemas.information_schemas import InformationResponse
router = APIRouter(
    prefix="/information",
    tags=["information"],
)


@router.get(
    "/@me",
    description="내 정보를 조회합니다."
)
def get_my_information(
    db: Session = Depends(get_db),
):
    # TODO: 데이터 조회
    tags = db.query(Keyword).all()
    friends = db.query(Friend).all()

    return InformationResponse(
        tags=tags,
        friends=friends
    )
