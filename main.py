from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Todo API")

class ItemCreate(BaseModel):
    title: str
    done: bool = False

class Item(ItemCreate):
    id: int

# 超シンプル：メモリに保存（コンテナ再起動すると消える）
_items: List[Item] = []
_next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=list[Item])
def list_items():
    return _items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    it = Item(id=_next_id, title=payload.title, done=payload.done)
    _items.append(it)
    _next_id += 1
    return it

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            updated = Item(id=item_id, title=payload.title, done=payload.done)
            _items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            _items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")