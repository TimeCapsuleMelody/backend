from typing import List

from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/keyword",
    tags=["keyword"],
)
