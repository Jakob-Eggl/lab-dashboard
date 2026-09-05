import os
from sqlmodel import SQLModel, create_engine, Session

DATA_DIR = os.environ.get("DATA_DIR", "/data")
os.makedirs(DATA_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATA_DIR}/labdata.db"

# check_same_thread=False is needed because FastAPI can use the connection
# from different threads; SQLite itself still only ever sees one request at a time here.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
