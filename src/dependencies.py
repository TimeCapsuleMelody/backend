from datetime import date

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql import and_

from database import get_db_session


def get_db():
    try:
        session = get_db_session()
        yield session
    finally:
        session.close()
