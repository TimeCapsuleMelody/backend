from typing import List

from fastapi import APIRouter, Depends, Query, status, HTTPException, Header
from fastapi.responses import FileResponse
import os
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/music",
    tags=["music"],
)


@router.get(
    "/by-id/{music_id}",
    description="음악 파일을 조회합니다."
)
async def stream_music(music_id: str):
    # 리소스 폴더 경로 설정
    resource_path = Path("resource")

    # 음악 파일 찾기 (예: music_id.mp3 형식으로 저장되었다고 가정)
    # music_name = music_id + ".mp3"

    music_name = "our dream.mp3"

    # 음악 파일 찾기 (예: music_id.mp3 형식으로 저장되었다고 가정)
    music_file = resource_path / music_name

    # 파일이 존재하는지 확인
    if not music_file.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Music file not found"
        )

    # 파일 응답
    return FileResponse(
        path=music_file,
        media_type="audio/mpeg",
        filename=music_file.name
    )


@router.get(
    "/streaming/{music_id}",
    description="음악 파일을 스트리밍합니다."
)
async def stream_music(music_id: str, range: str = Header(None)):
    resource_path = Path("resource")
    music_name = "our dream.mp3"
    music_file = resource_path / music_name

    if not music_file.exists():
        raise HTTPException(status_code=404, detail="File not found")

    file_size = music_file.stat().st_size

    # Range 헤더 처리
    start = 0
    end = file_size - 1

    if range is not None:
        start, end = range.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1

    # 실제 전송할 크기
    chunk_size = end - start + 1

    # 파일 스트리밍
    async def ranged_file_sender():
        with open(music_file, mode="rb") as file:
            file.seek(start)
            remaining = chunk_size
            while remaining > 0:
                chunk_size = min(1024 * 1024, remaining)  # 최대 1MB씩 전송
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                remaining -= len(chunk)
                yield chunk

    headers = {
        'Content-Range': f'bytes {start}-{end}/{file_size}',
        'Accept-Ranges': 'bytes',
        'Content-Length': str(chunk_size),
        'Content-Disposition': f'attachment; filename="{music_name}"'
    }

    return StreamingResponse(
        ranged_file_sender(),
        status_code=206 if range else 200,
        media_type='audio/mpeg',
        headers=headers
    )


class Music(BaseModel):
    musicId: int
    musicTitle: str
    date: str
    friend: str
    diary: str
    feeling: int
    keywords: List[str]
    image: str


# 2. GET /by-period
"""
response
{
music을 날짜에 맞게 묶어서 반환
년-월 별로 묶어서 반환
}
"""


class MusicByPeriod(BaseModel):
    year: int
    month: int
    music: List[Music]


@router.get(
    "/by-period",
    response_model=List[MusicByPeriod],
    description="음악을 년-월 별로 묶어서 반환합니다."
)
async def get_music_by_period():
    # mock 5개
    return [
        MusicByPeriod(year=2024, month=1, music=[Music(musicId=1, musicTitle="our dream", date="2024-01-01",
                      friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="image1")]),
        MusicByPeriod(year=2024, month=2, music=[Music(musicId=2, musicTitle="our dream", date="2024-02-01", friend="friend2", diary="diary2", feeling=2, keywords=["keyword1", "keyword2"], image="image2"),
                                                 Music(musicId=3, musicTitle="our dream", date="2024-02-01", friend="friend3", diary="diary3", feeling=3, keywords=["keyword1", "keyword2"], image="image3")]),
        MusicByPeriod(year=2024, month=3, music=[Music(musicId=3, musicTitle="our dream", date="2024-03-01",
                      friend="friend3", diary="diary3", feeling=3, keywords=["keyword1", "keyword2"], image="image3")]),
        MusicByPeriod(year=2024, month=4, music=[Music(musicId=4, musicTitle="our dream", date="2024-04-01",
                      friend="friend4", diary="diary4", feeling=4, keywords=["keyword1", "keyword2"], image="image4")]),
        MusicByPeriod(year=2024, month=5, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                      friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="image5")]),
    ]

# 3. GET /by-keyword/{keyword}
@router.get(
    "/by-keyword/{keyword}",
    description="키워드에 맞는 음악을 반환합니다."
)
async def get_music_by_keyword(keyword: str):
    return [
        Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="image1")
    ]

# 3. GET /by-friend/{friend}
@router.get(
    "/by-friend/{friend}",
    description="친구에 맞는 음악을 반환합니다."
)
async def get_music_by_friend(friend: str):
    return [
        Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="image1")
    ]

# 3. GET /search