from sqlmodel import SQLModel, Session
import sqlmodel
import timescaledb

from .config import Database_url, Database_timezone

if Database_url == '' :
    raise NotImplementedError("The database not yet been implemented")

engine = timescaledb.create_engine(Database_url, timezone=Database_timezone)

def init_db() :
    print("establish connection")
    SQLModel.metadata.create_all(engine)
    print("initializing hyper_tables")
    timescaledb.metadata.create_all(engine)

def getSession():
    with Session(engine) as session:
        yield session