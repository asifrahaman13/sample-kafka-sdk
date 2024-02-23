# Import all the packages and modules required for the FastAPI server.
from example_package_asifr_berhampore.example_package_asifr_berhampore import (
    TrafficProcessingSDK,
)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool

# Create an instance of the FastAPI class.
app = FastAPI()

# Define the origins for the CORS middleware.
origins = [
    "*",
]

# Add middlewares to the origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of the TrafficProcessingSDK class and consume
kafka_bootstrap_servers = "localhost:9092"
group_id = "traffic-processing-group"
sdk = TrafficProcessingSDK(kafka_bootstrap_servers, group_id)


# Create a sample middleware. 
@app.middleware("http")
async def some_middleware(request: Request, call_next):
    response = await call_next(request)
    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    print(f"response_body={response_body[0].decode()}")
    print(request.url.path)
    print(request.method)

    sdk.process_request(request.url.path, request.method, response_body[0].decode())
    return response


# Sample data for demonstration
data = {"1": "item1", "2": "item2"}


# GET endpoint to retrieve all items
@app.get("/")
async def read_items():
    return {"message": "Welcome to the FastAPI server"}


@app.get("/items/")
async def read_items():
    return data


# GET endpoint to retrieve a single item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    return {item_id: data[item_id]}


# POST endpoint to add a new item
@app.post("/items/")
async def create_item(item_id: str, item_name: str):
    data[item_id] = item_name
    return {"message": "Item added successfully"}


# PUT endpoint to update an existing item
@app.put("/items/{item_id}")
async def update_item(item_id: str, item_name: str):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    data[item_id] = item_name
    return {"message": "Item updated successfully"}


# DELETE endpoint to delete an existing item
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    del data[item_id]
    return {"message": "Item deleted successfully"}
