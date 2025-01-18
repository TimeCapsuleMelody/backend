from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status, HTTPException, Header
from fastapi.responses import FileResponse
import os
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = 'AIzaSyB0CxgntcjKXRPU_3E4FtrhqfhpnLE1IQE'


async def get_youtube_service():
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

router = APIRouter(
    prefix="/music",
    tags=["music"],
)


@router.get("/streaming/{music_id}")
async def stream_music(music_id: str):
    resource_path = Path("resource")
    music_name = "our dream.mp3"
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


@router.get(
    "/by-keyword/{keyword}",
    description="키워드에 맞는 음악을 반환합니다."
)
async def get_music_by_keyword(keyword: str):
    return [
        Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1",
              diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="image1")
    ]


@router.get(
    "/by-friend/{friend}",
    description="친구에 맞는 음악을 반환합니다."
)
async def get_music_by_friend(friend: str):
    return [
        Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1",
              diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="image1")
    ]

# 3. GET /search
# 프론트에서 request로 검색하고자 하는 음악을 string으로 주면 유튜브에서 해당 음악을 검색한 결과 리스트를 반환합니다


class SearchMusicResponse(BaseModel):
    title: str
    thumbnail: str
    url: str


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
