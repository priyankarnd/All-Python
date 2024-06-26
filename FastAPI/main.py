from fastapi import FastAPI

app = FastAPI()

# Get parameter
@app.get("/")
async def root():
    return {"message" : "Hello World"}

'''
# Get an item by ID
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
'''

# Path parameters with types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Ordering of paths
# Fixed path should be declared before variable path. Otherwise, the fixed value will be treated as variable.

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

