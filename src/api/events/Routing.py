from fastapi import APIRouter

from .models import (EventSchema,
    EventListSchema,
    EventEventSchema,
    CreateEventSchema,
    UpdateEventSchema)

from api.db.config import Database_url

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
@router.get('/')
def getItems() -> EventListSchema:
    return {
        'items' : [1,2,3]
    }

@router.post('/')
def createItem(payload : CreateEventSchema) -> EventListSchema:
    print(payload)
    return {
        'items' : [1,2,3]
    }

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
@router.get('/{event_id}')
def getItems(event_id : int)  -> EventSchema :
    print("Database_url :",Database_url)
    return {
        'id' : event_id,
        'path' : 'localhost'
    }

@router.post('/{event_id}')
def createItem(event_id : int, payload : CreateEventSchema) -> EventSchema:
    data = payload.model_dump() #payload -> dict
    print("data :",*data)
    return {
        'id' : event_id,
        **data
    }

@router.put('/{event_id}')
def updateItem(event_id : int, payload : UpdateEventSchema) -> EventSchema:
    data = payload.model_dump() #payload -> dict
    return {
        'id' : event_id,
        **data
    }





