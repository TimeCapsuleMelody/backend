from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/music",
    tags=["music"],
)

# 1. GET /streaming/{music_id}

# 2. GET /by-period

# 3. GET /by-keyword

# 3. GET /search