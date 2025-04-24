# from pydantic import BaseModel, Field
from typing import List, Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

import sqlmodel
from timescaledb import TimescaleModel

def get_utc_time() :
    return datetime.now(timezone.utc)

class EventModel(TimescaleModel, table=True) :
    # id : int = Field(primary_key= True, default=None)
    path : str = Field(
        index=True,
        default=''
    )
    description : Optional[str] = ''
    # created_at : datetime = Field(
    #     default = get_utc_time(),
    #     sa_type=sqlmodel.DateTime(timezone=True),
    #     nullable= False
    # )
    updated_at : datetime = Field(
        default = get_utc_time(),
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable= False
    )

    __chunk_time_interval__: str = "INTERVAL 1 day"
    __drop_after__: str = "INTERVAL 6 months"

# class EventModel(SQLModel, table=True) :
#     id : int = Field(primary_key= True, default=None)
#     path : Optional[str] = ''
#     description : Optional[str] = ''
#     created_at : datetime = Field(
#         default = get_utc_time(),
#         sa_type=sqlmodel.DateTime(timezone=True),
#         nullable= False
#     )
#     updated_at : datetime = Field(
#         default = get_utc_time(),
#         sa_type=sqlmodel.DateTime(timezone=True),
#         nullable= False
#     )

class EventSchema(SQLModel) :
    id : int = Field(primary_key= True, default='')
    path : Optional[str] = ''
    description : Optional[str] = ''
    created_at : datetime = Field(
        default = datetime.now(timezone.utc),
        nullable= False
    )
    updated_at : datetime = Field(
        default = datetime.now(timezone.utc),
        nullable= False
    )

class EventListSchema(SQLModel) :
    items : list[int]

class EventBucketSchema(SQLModel) :
    bucket : datetime
    path : str
    count : int

class EventEventSchema(SQLModel) :
    items : List[EventSchema]
    count : int

class EventListModel(SQLModel) :
    items : List[EventModel]

class CreateEventSchema(SQLModel) :
    path : str
    description : Optional[str] = 'api'

class UpdateEventSchema(SQLModel) :
    description : str