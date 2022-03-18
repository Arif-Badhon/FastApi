#import all
from fastapi import FastAPI

#start fastapi
app = FastAPI()

#modules
@app.get("/")
def index():
    return {"Name": "Badhon"}