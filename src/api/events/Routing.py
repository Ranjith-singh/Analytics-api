from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, delete, func

from .models import (EventSchema,
    EventListSchema,
    EventEventSchema,
    EventListModel,
    CreateEventSchema,
    UpdateEventSchema,
    EventModel,
    EventBucketSchema)
    # get_utc_time)

from api.db.config import Database_url
from api.db.session import getSession

from timescaledb.utils import get_utc_now
from timescaledb.hyperfunctions import time_bucket

router = APIRouter()

# @router.get('/')
# def getItems() :
#     return {
#         'items' : [1,2]
#     }

@router.get('/list')
def getItems() -> EventEventSchema:
    return {
        'items' : [{'id' : 1},{'id' : 2},{'id' : 3}],
        'count' : 3
    }

# root path
# @router.get('/',response_model=EventListModel)
# def getItems(session : Session = Depends(getSession)):
#     query = select(EventModel).order_by(EventModel.id.desc()).limit(5)
#     data = session.exec(query).fetchall()
#     print("data :",data)
#     return {
#         'items' : data
#     }

@router.get('/',response_model=List[EventBucketSchema])
def getItems(
    duration : str = Query(default="1 day"),
    paths : List = Query(default=['/about','/signup','/login','/dashboard']),
    session : Session = Depends(getSession)
    ):
    bucket = time_bucket(duration, EventModel.time)
    print("paths :",paths)
    query = (select(bucket.label('bucket'),
                EventModel.path.label('path'),
                func.count().label('count'))
            .where(
                EventModel.path.in_(paths)
            )
            .group_by(
                bucket,
                EventModel.path
            )
            .order_by(
                bucket,
                EventModel.path
            ))
    data = session.exec(query).fetchall()
    return data

@router.post('/', response_model=EventModel)
def createItem(payload : CreateEventSchema, session : Session = Depends(getSession)):
    data = payload.model_dump()
    print("data :",data)
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.put('/')
def updateItem(payload : UpdateEventSchema) -> EventListSchema:
    print(payload)
    return {
        'items' : [1,2,3]
    }

@router.delete('/')
def deleteItem(items : dict = {}) -> EventListSchema:
    return {
        'items' : [1,2,3]
    }


# parameter
@router.get('/{event_id}', response_model=EventModel)
def getItems(event_id : int, session : Session = Depends(getSession)) :
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if result is None:
        raise HTTPException(status_code=404,detail="Event not found")
    # obj = EventModel.model_validate(result)
    return result

@router.post('/{event_id}', response_model=EventSchema)
def createItem(event_id : int, payload : CreateEventSchema, session : Session = Depends(getSession)):
    query = select(EventModel).where(EventModel.id == event_id)
    data = payload.model_dump() #payload -> dict
    print("data :",*data)
    return {
        'id' : event_id,
        **data
    }

@router.put('/{event_id}', response_model=EventSchema)
def updateItem(event_id : int, payload : UpdateEventSchema, session : Session = Depends(getSession)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    data = payload.model_dump() #payload -> dict
    # print("data :",data)
    for key, value in data.items():
        setattr(obj, key, value)
    obj.updated_at = get_utc_now()
    EventModel.model_validate(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.delete('/{event_id}', response_model=EventListModel)
def deleteItem(event_id : int, session : Session = Depends(getSession)):
    # query = select(EventModel).where(EventModel.id == event_id)
    query = delete(EventModel).where(EventModel.id == event_id).returning(EventModel)
    obj = session.exec(query).all()
    session.commit()
    # session.refresh(obj)
    # print("obj :",obj)
    return {
        'items' : obj
    }





