from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, Query, status, HTTPException
from pydantic import BaseModel, Field

from botocore.config import Config
import boto3

from config import settings

router = APIRouter(
    prefix="",
    tags=["photo"],
)

# S3 클라이언트 설정
s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
    config=Config(signature_version='s3v4')
)


@router.get(
    "/presigned-url",
    description="사진 업로드를 위한 S3 presigned URL을 발급합니다."
)
async def get_presigned_url(file_name: str):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_file_name = f"{timestamp}_{file_name}"

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
