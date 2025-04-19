from fastapi import APIRouter

from .Schemas import EventSchema,EventListSchema,EventEventSchema

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

@router.get('/{event_id}')
def getItems(event_id : int)  -> EventSchema :
    return {
        'id' : event_id,
        'ido' : event_id
    }

@router.get('/')
def getItems() -> EventListSchema:
    return {
        'items' : [1,2,3]
    }

@router.post('/')
def createItem(items : dict = {}) -> EventListSchema:
    print(items)
    return {
        'items' : [1,2,3]
    }

@router.put('/')
def updateItem(payload : dict = {}) -> EventListSchema:
    return {
        'items' : [1,2,3]
    }

@router.delete('/')
def deleteItem(items : dict = {}) -> EventListSchema:
    return {
        'items' : [1,2,3]
    }

