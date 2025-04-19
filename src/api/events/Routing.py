from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def getItems() :
    return {
        'items' : [1,2,3]
    }