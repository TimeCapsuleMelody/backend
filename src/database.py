from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


class EngineConnection:
    def __init__(self):
        SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, pool_recycle=500, connect_args={"connect_timeout": 100})
        self.session_local = sessionmaker(
            autoflush=False, autocommit=False, bind=self.engine)

    def get_session(self):
        return self.session_local()

    def get_connection(self):
        return self.engine.connect()


engine_conn = EngineConnection()


def get_db_session():
    session = engine_conn.get_session()
    return session
