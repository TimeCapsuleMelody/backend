from domain.schemas.music_schemas import Music, MusicByPeriod

MOCK_IMAGE_URL = "https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"

MOCK_MUSIC_BY_PERIOD = [
    MusicByPeriod(year=2024, month=1, music=[
        Music(musicId=1, musicTitle="our dream", date="2024-01-01",
                  friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=10, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=11, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=12, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=13, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=15, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")
    ]),
    MusicByPeriod(year=2024, month=2, music=[Music(musicId=2, musicTitle="our dream", date="2024-02-01", friend="friend2", diary="diary2", feeling=2, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
                                             Music(musicId=3, musicTitle="our dream", date="2024-02-01", friend="friend3", diary="diary3", feeling=3, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=3, music=[Music(musicId=3, musicTitle="our dream", date="2024-03-01",
                                                   friend="friend3", diary="diary3", feeling=3, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=4, music=[Music(musicId=4, musicTitle="our dream", date="2024-04-01",
                                                   friend="friend4", diary="diary4", feeling=4, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=5, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                   friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=6, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                   friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=7, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                   friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=8, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                   friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=9, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                   friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2024, month=10, music=[Music(musicId=5, musicTitle="our dream", date="2024-05-01",
                                                    friend="friend5", diary="diary5", feeling=5, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")]),
    MusicByPeriod(year=2025, month=1, music=[
        Music(musicId=1, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=10, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=11, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=12, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=13, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg"),
        Music(musicId=15, musicTitle="our dream", date="2024-01-01",
              friend="friend1", diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")
    ]),
]


MOCK_MUSIC_BY_KEYWORD = [
    Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1",
          diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")
]

MOCK_MUSIC_BY_FRIEND = [
    Music(musicId=1, musicTitle="our dream", date="2024-01-01", friend="friend1",
          diary="diary1", feeling=1, keywords=["keyword1", "keyword2"], image="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2022%2F08%2Fone-piece-luffys-anime-voice-actress-says-she-doesnt-read-the-manga-01.jpg")
]
