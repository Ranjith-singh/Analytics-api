from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel) :
    id : int

class EventListSchema(BaseModel) :
    items : list[int]

class EventEventSchema(BaseModel) :
    items : List[EventSchema]
    count : int