from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model for JSON input
class User(BaseModel):
    name: str
    age: int

# GET endpoint
@app.get("/test")
def test_api():
    return {"message": "API is working successfully!"}

# POST endpoint
@app.post("/submit")
def submit_data(user: User):
    return {
        "message": "Data received",
        "name": user.name,
        "age": user.age
    }
