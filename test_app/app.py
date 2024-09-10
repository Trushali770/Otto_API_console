from fastapi import FastAPI, Query,  Request
from typing import Optional

from library_package.mylib import get_data_from_jsonplaceholder, post_data  # Importing the updated function

app = FastAPI()

@app.get("/test-jsonplaceholder")
def test_jsonplaceholder(endpoint: str, post_id: Optional[int] = None):
    # Adding 'post_id' as a query parameter if provided
    params = {"id": post_id} if post_id else None

    # Call the library function that interacts with JSONPlaceholder
    response = get_data_from_jsonplaceholder(endpoint, params)

    # Return the response back to the client
    return response
    
@app.post("/test-post-endpoint")
async def test_post_endpoint(request: Request):
    # Receive JSON payload from client
    payload = await request.json()

    # Call the library function to post the data to JSONPlaceholder
    response = post_data('posts', payload)

    # Return the response back to the client
    return response