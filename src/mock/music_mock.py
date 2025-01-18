from domain.schemas.music_schemas import Music, MusicByPeriod

MOCK_IMAGE_URL = "https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"

MOCK_MUSIC = [
    MusicByPeriod(year=2024, month=1, music=[
        Music(musicId=1, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=10, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=11, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=12, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=13, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=15, musicTitle="our dream", date="2024-01-01",
              friends=["friend1"], diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL)
    ]),
    MusicByPeriod(year=2024, month=2, music=[
        Music(musicId=2, musicTitle="our dream", date="2024-02-01",
              friends=["friend2"], diary="diary2", feeling=2, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL),
        Music(musicId=3, musicTitle="our dream", date="2024-02-01",
              friends=["friend3"], diary="diary3", feeling=3, keywords=["keyword1", "keyword2"], image=MOCK_IMAGE_URL)
    ]),
    # ... Rest of the months follow the same pattern
]
