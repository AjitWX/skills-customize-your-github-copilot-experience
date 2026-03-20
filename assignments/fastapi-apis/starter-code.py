from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.get("/search")
async def search_items(q: str, limit: int = 10):
    return {"query": q, "limit": limit, "results": []}

@app.post("/items")
async def create_item(item: Item):
    price_with_tax = item.price + (item.tax or 0)
    return {**item.dict(), "price_with_tax": price_with_tax}
