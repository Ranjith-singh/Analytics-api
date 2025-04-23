# from pydantic import BaseModel, Field
from typing import List, Optional
from sqlmodel import SQLModel, Field

class EventModel(SQLModel, table=True) :
    id : int = Field(primary_key= True, default=None)
    path : Optional[str] = ''
    description : Optional[str] = ''

class EventSchema(SQLModel) :
    id : int = Field(primary_key= True, default='')
    path : Optional[str] = ''
    description : Optional[str] = ''

class EventListSchema(SQLModel) :
    items : list[int]

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