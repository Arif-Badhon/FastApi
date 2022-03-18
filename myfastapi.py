#import all
from fastapi import FastAPI

#start fastapi
app = FastAPI()

#Dummy Data
students = {
    1 : {
        "Name":"Badhon",
        "age": 28,
        "designation": "Data Specialist"
    }
}
#modules
@app.get("/")
def index():
    return {"Name": "Badhon"}

@app.get("/get-data/{student_id}")
def get_data(student_id: int):
    return students[student_id]