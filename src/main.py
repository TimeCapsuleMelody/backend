from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from route.friend_route import router as friend_route
from route.music_route import router as music_route
from route.information_route import router as information_route
from route.photo_route import router as photo_route
import boto3
from botocore.config import Config
import os
from datetime import datetime

from config import settings


# S3 클라이언트 설정
s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
    config=Config(signature_version='s3v4')
)

app = FastAPI(
    title="Time Capsule Melody",
    version="0.0.1",
    description="Time Capsule Melody API",
    contact={
        "name": "권민재",
        "url": "https://mindorizip.tistory.com/",
        "email": "mjkweon17@korea.ac.kr",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/Time-Capsule-Melody/time-capsule-melody/blob/main/LICENSE",
    },
)

# CORS
origins = [
    "http://localhost:3000",
    "https://time-capsule-melody.vercel.app/",
    "https://time-capsule-melody.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin", "Authorization"]
)

app.include_router(friend_route)
app.include_router(music_route)
app.include_router(information_route)
app.include_router(photo_route)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/presigned-url")
async def get_presigned_url(file_name: str):
    # try:
    # 파일 이름에 타임스탬프 추가하여 유니크한 키 생성
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_file_name = f"{timestamp}_{file_name}"

    # presigned URL 생성 (유효시간: 3600초 = 1시간)
    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': settings.AWS_BUCKET_NAME,
            'Key': unique_file_name,
            'ContentType': 'application/octet-stream'
        },
        ExpiresIn=3600
    )

    return {
        "presigned_url": presigned_url,
        "file_key": unique_file_name
    }
    # except Exception as e:
    #     # raise HTTPException(status_code=500, detail=str(e))
    #     println(e)
    #     return {"error": str(e)}
