from sqlalchemy import TIMESTAMP, Boolean, Column, Date, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Memory(Base):
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    music_title = Column(String(1000), nullable=False)
    music_link = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now(), nullable=False)
    friend = Column(String(50), nullable=False)
    diary = Column(Text, nullable=False)
    feeling = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    photo_id = Column(Integer, nullable=False)

    # Relationships with foreign() for explicit foreign key relationships
    photo = relationship(
        "Photo",
        primaryjoin="foreign(Memory.photo_id) == Photo.id",
        viewonly=True
    )
    friends = relationship(
        "Friend",
        secondary="memory_friend_mapping",
        primaryjoin="Memory.id == MemoryFriendMapping.memory_id",
        secondaryjoin="foreign(MemoryFriendMapping.friend_id) == Friend.id",
        viewonly=True
    )
    keywords = relationship(
        "Keyword",
        secondary="memory_keyword_mapping",
        primaryjoin="Memory.id == MemoryKeywordMapping.memory_id",
        secondaryjoin="foreign(MemoryKeywordMapping.keyword_id) == Keyword.id",
        viewonly=True
    )


class Friend(Base):
    __tablename__ = "friend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now(), nullable=False)

    # Relationships
    memories = relationship(
        "Memory",
        secondary="memory_friend_mapping",
        primaryjoin="Friend.id == MemoryFriendMapping.friend_id",
        secondaryjoin="foreign(MemoryFriendMapping.memory_id) == Memory.id",
        viewonly=True
    )


class MemoryFriendMapping(Base):
    __tablename__ = "memory_friend_mapping"
    id = Column(Integer, primary_key=True, autoincrement=True)
    memory_id = Column(Integer, nullable=False)
    friend_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    memory = relationship(
        "Memory",
        primaryjoin="foreign(MemoryFriendMapping.memory_id) == Memory.id",
        viewonly=True
    )
    friend = relationship(
        "Friend",
        primaryjoin="foreign(MemoryFriendMapping.friend_id) == Friend.id",
        viewonly=True
    )


class Keyword(Base):
    __tablename__ = "keyword"
    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    memories = relationship(
        "Memory",
        secondary="memory_keyword_mapping",
        primaryjoin="Keyword.id == MemoryKeywordMapping.keyword_id",
        secondaryjoin="foreign(MemoryKeywordMapping.memory_id) == Memory.id",
        viewonly=True
    )


class MemoryKeywordMapping(Base):
    __tablename__ = "memory_keyword_mapping"
    id = Column(Integer, primary_key=True, autoincrement=True)
    memory_id = Column(Integer, nullable=False)
    keyword_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    memory = relationship(
        "Memory",
        primaryjoin="foreign(MemoryKeywordMapping.memory_id) == Memory.id",
        viewonly=True
    )
    keyword = relationship(
        "Keyword",
        primaryjoin="foreign(MemoryKeywordMapping.keyword_id) == Keyword.id",
        viewonly=True
    )


class Photo(Base):
    __tablename__ = "photo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_url = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now(), nullable=False)

    # Relationships
    memories = relationship(
        "Memory",
        primaryjoin="foreign(Photo.id) == Memory.photo_id",
        viewonly=True
    )
