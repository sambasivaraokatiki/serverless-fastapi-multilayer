from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

# Configure CORS
origins = [
    "*",
    # Add more allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your API routes here
@app.get("/")
def read_root():
    """
    Root endpoint of the API.

    Returns:
        dict: A dictionary with the message "Hello: World".
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Endpoint to read an item by its ID.

    Args:
        item_id (int): The ID of the item.
        q (str, optional): A query parameter.

    Returns:
        dict: A dictionary with the item ID and the query parameter.
    """
    return {"item_id": item_id, "q": q}

# Create a Mangum handler for AWS Lambda
handler = Mangum(app)