from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from route.friend_route import router as friend_route
from route.music_route import router as music_route
from src.route.information_route import router as information_route
from route.photo_route import router as photo_route


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