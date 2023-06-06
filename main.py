from fastapi import FastAPI
from typing import Optional
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    booking: str
    email: str
    date: str
    time: str
    content: str

class ItemUpdate(BaseModel):
    booking: str
    email: str
    date: str
    time: str
    content: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

list_item = []

@app.get("/items/")
async def get_item():
    return list_item

@app.post("/items/")
async def create_item(item: Item):
    list_item.append(item)
    return {"id":item.id}

@app.delete("/items/{item_id}")
async def delete_item(item_id: UUID):
    for item in list_item:
        if item.id == item_id:
            list_item.remove(item)
            return
        
@app.put("/items/{item_id}")
async def update_item(item_update: ItemUpdate, item_id: UUID):
    for item in list_item:
        if item.id == item_id:
            if item_update.booking is not None:
                item.booking = item_update.booking
            if item_update.date is not None:
                item.date = item_update.date
            if item_update.time is not None:
                item.time = item_update.time
            if item_update.content is not None:
                item.content = item_update.content
            return
