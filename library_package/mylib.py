import requests

base_url = "https://jsonplaceholder.typicode.com/"
def get_data_from_jsonplaceholder(endpoint, params=None):
    url = f"{base_url}{endpoint}"
    
    # Making a GET request to JSONPlaceholder
    response = requests.get(url, params=params)
    
    # Returning the response as JSON
    return response.json()

def post_data(endpoint, payload):
    url = f"{base_url}{endpoint}"
    response = requests.post(url, json=payload)
    return response.json()