'''
A request body is data sent by the client to your API. A response body is the data your API sends to the client. 
Your API almost always has to send a response body. But clients don’t necessarily need to send request bodies all 
the time.
'''
# Request body using pydantic

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# description and tax are optional because they have a default value of None. A json object without these two fields are also valid.

app = FastAPI()

# Adding the new pydantic model to the path operation as a parameter

@app.post("/items/")
async def create_item(item: Item):
    return item


# Receiving what is in function instead of dict
@app.post("/itemsupdt/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Declare path parameters and a request body at the same time
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
