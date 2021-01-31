from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

tempDB = []


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_avalaible: Optional[bool] = None


@app.get("/")
def read_root():
    return {"greetings": "Welcome to my website"}


@app.get("/items")
def get_items():

    # print(uuid.uuid4())
    return tempDB


@app.get("/items/{item_id}")
def get_an_item(item_id: int):
    item = item_id - 1
    return tempDB[item]


@app.post("/items")
def add_item(item: Item):
    tempDB.append(item.dict())
    return tempDB[-1]


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    tempDB.pop(item_id-1)
    return {"action": "Item deleted successfully"}
