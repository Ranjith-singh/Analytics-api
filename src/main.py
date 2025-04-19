from typing import Union

from fastapi import FastAPI

from api.events import router as eventRouter 

app = FastAPI()
app.include_router(eventRouter,prefix=f'/api/events')

@app.get("/")
def read_root():
    return {"Hello": "Worlds"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
def readHealthStatus():
    return {"status": "ok"}



