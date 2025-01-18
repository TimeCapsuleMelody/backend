import os
from pathlib import Path
from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from fastapi.responses import FileResponse, StreamingResponse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import settings
from domain.schemas.music_schemas import (Music, MusicByPeriod,
                                          SearchMusicResponse)
from mock.music_mock import MOCK_MUSIC
from dependencies import get_db

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY


async def get_youtube_service():
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

router = APIRouter(
    prefix="/music",
    tags=["music"],
)


@router.get("/streaming/{music_id}")
async def stream_music(
    music_id: str,
    db: Session = Depends(get_db),
):
    resource_path = Path("resource")
    music_name = "our dream.mp3"
    if (music_id == 15):
        music_name = "duck fly.mp3"

    music_file = resource_path / music_name

    if not music_file.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Music file not found"
        )

    # 파일을 chunk 단위로 읽어서 전송하는 함수
    def iterfile():
        CHUNK_SIZE = 1024 * 1024  # 1MB 단위로 전송
        with open(music_file, mode="rb") as file_like:
            while chunk := file_like.read(CHUNK_SIZE):
                yield chunk

    # 스트리밍 응답 생성
    return StreamingResponse(
        iterfile(),
        media_type="audio/mpeg",
        headers={
            'Content-Disposition': f'attachment; filename="{music_name}"',
            'Accept-Ranges': 'bytes'
        }
    )


@router.get(
    "/by-period",
    response_model=List[MusicByPeriod],
    description="음악을 년-월 별로 묶어서 반환합니다.",
    deprecated=True,
)
async def get_music_by_period(
        db: Session = Depends(get_db)
):
    return MOCK_MUSIC


@router.get(
    "/by-keyword/{keyword}",
    description="키워드에 맞는 음악을 반환합니다.",
    deprecated=True,
)
async def get_music_by_keyword(
    keyword: str,
    db: Session = Depends(get_db)
):
    return MOCK_MUSIC


@router.get(
    "/by-friend/{friend}",
    description="친구에 맞는 음악을 반환합니다.",
    deprecated=True,
)
async def get_music_by_friend(
    friend: str,
    db: Session = Depends(get_db)
):

    # matching_music = [
    #     music for music in MOCK_MUSIC_BY_FRIEND
    #     if friend in music.friends
    # ]
    # return matching_music

    return MOCK_MUSIC


@router.get(
    "/search",
    response_model=List[SearchMusicResponse],
    description="유튜브에서 검색한 음악을 반환합니다."
)
async def search_music(query: str, max_results: Optional[int] = 3):
    youtube = await get_youtube_service()

    # YouTube API 검색 요청
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type='video',
        videoCategoryId='10'  # Music category
    ).execute()

    # 검색 결과 변환
    results = []
    for item in search_response.get('items', []):
        video_id = item['id']['videoId']
        snippet = item['snippet']

        result = SearchMusicResponse(
            title=snippet['title'],
            thumbnail=snippet['thumbnails']['high']['url'],
            url=f"https://www.youtube.com/watch?v={video_id}"
        )
        results.append(result)

    return results
