from fastapi import APIRouter

from .Schemas import EventSchema

router = APIRouter()

@router.get('/')
def getItems() :
    return {
        'items' : [1,2,3]
    }

@router.get('/{event_id}')
def getItems(event_id : int)  -> EventSchema :
    return {
        'id' : event_id,
        'ido' : event_id
    }