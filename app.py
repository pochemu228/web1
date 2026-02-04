from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def read_root():
    return {"message": "Hi!"}