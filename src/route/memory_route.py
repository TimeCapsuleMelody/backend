from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query, status

from repository.models import Friend, Keyword, MemoryFriendMapping, MemoryKeywordMapping, Memory
from dependencies import get_db
from domain.schemas.music_schemas import Music

router = APIRouter(
    prefix="/memory",
    tags=["memory"],
)


@router.post(
    "/",
    description="Music(추억)을 저장합니다.",
)
async def save_music(
    music: Music,
    db: Session = Depends(get_db),
):
    # 전처리: Keyword에 공백 제거
    music.keywords = [keyword.strip() for keyword in music.keywords]

    # 1. Friend 테이블에 없는 friends가 있는지 확인하고 없으면 추가
    for friend in music.friends:
        friend_obj = db.query(Friend).filter(Friend.name == friend).first()
        if not friend_obj:
            friend_obj = Friend(name=friend)
            db.add(friend_obj)
            db.commit()
            db.refresh(friend_obj)

    # 2. Keyword 테이블에 없는 keywords가 있는지 확인하고 없으면 추가
    for keyword in music.keywords:
        keyword_obj = db.query(Keyword).filter(
            Keyword.keyword == keyword).first()
        if not keyword_obj:
            keyword_obj = Keyword(keyword=keyword)
            db.add(keyword_obj)
            db.commit()
            db.refresh(keyword_obj)

    # 3. Memory 테이블에 데이터 저장
    memory_obj = Memory(
        music_title=music.musicTitle,
        music_link="",  # music_link는 필수 필드이므로 값을 제공해야 함
        diary=music.diary,
        feeling=music.feeling,
        friend="",  # friend는 필수 필드이므로 값을 제공해야 함
        image=music.image,
        photo_id=0  # photo_id는 필수 필드이므로 값을 제공해야 함
    )
    db.add(memory_obj)
    db.commit()
    db.refresh(memory_obj)

    # 4. mapping 테이블에 데이터 저장
    for friend in music.friends:
        friend_obj = db.query(Friend).filter(Friend.name == friend).first()
        memory_friend_mapping_obj = MemoryFriendMapping(
            memory_id=memory_obj.id,
            friend_id=friend_obj.id,
        )
        db.add(memory_friend_mapping_obj)
    db.commit()

    for keyword in music.keywords:
        keyword_obj = db.query(Keyword).filter(
            Keyword.keyword == keyword).first()
        memory_keyword_mapping_obj = MemoryKeywordMapping(
            memory_id=memory_obj.id,
            keyword_id=keyword_obj.id,
        )
        db.add(memory_keyword_mapping_obj)
    db.commit()

    return {"message": "Music saved successfully"}
