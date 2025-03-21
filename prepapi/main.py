# set up fastapi app
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    """
    Root endpoint
    Args:
        None
    Returns:
        dict: message
    """
    return {"message": "Hello World!"}

@app.get("/greet/{name}")
def greet(name: str) -> dict:
    """
    Greet endpoint
    Args:
        name (str): name to greet
    Returns:
        dict: message
    """
    return {"message": f"Hello, {name}!"}