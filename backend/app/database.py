import os
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import inspect, text

DATA_DIR = os.environ.get("DATA_DIR", "/data")
os.makedirs(DATA_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATA_DIR}/labdata.db"

# check_same_thread=False is needed because FastAPI can use the connection
# from different threads; SQLite itself still only ever sees one request at a time here.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Lightweight, additive schema migrations. create_all() only creates *missing*
# tables - it never alters an existing table - so whenever a new column is
# added to a model here, add a matching entry below. This lets people update
# the code without losing their existing SQLite database.
# Format: {table_name: {column_name: "SQL type for ALTER TABLE ... ADD COLUMN"}}
_COLUMN_MIGRATIONS = {
    "parameteroverride": {
        "unit": "VARCHAR",
    },
}


def _run_migrations():
    inspector = inspect(engine)
    existing_tables = set(inspector.get_table_names())

    with engine.begin() as conn:
        for table, columns in _COLUMN_MIGRATIONS.items():
            if table not in existing_tables:
                continue  # brand-new install: create_all() already made it with all columns
            existing_columns = {c["name"] for c in inspector.get_columns(table)}
            for column, sql_type in columns.items():
                if column not in existing_columns:
                    conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {sql_type}"))


def init_db():
    SQLModel.metadata.create_all(engine)
    _run_migrations()


def get_session():
    with Session(engine) as session:
        yield session

