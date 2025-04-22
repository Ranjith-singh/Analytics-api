from sqlmodel import SQLModel, Session
import sqlmodel

from .config import Database_url

if Database_url == '' :
    raise NotImplementedError("The database not yet been implemented")

engine = sqlmodel.create_engine(Database_url)

def init_db() :
    print("establish connection")
    SQLModel.metadata.create_all(engine)