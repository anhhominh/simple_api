from fastapi import FastAPI
from typing import Optional
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

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

db: List[Item] = []

@app.get("/items/")
async def get_item():
    return db

@app.post("/items/")
async def create_item(item: Item):
    db.append(item)
    return {"id":item.id}

@app.delete("/items/{item_id}")
async def delete_item(item_id: UUID):
    for item in db:
        if item.id == item_id:
            db.remove(item)
            return
        
@app.put("/items/{item_id}")
async def update_item(item_update: ItemUpdate, item_id: UUID):
    for item in db:
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
