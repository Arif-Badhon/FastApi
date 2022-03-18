#import all
from fastapi import FastAPI, Path

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

#path parameter
@app.get("/get-data/{student_id}")
def get_data(student_id: int = Path(None, description="Id must be in student", gt=0)):
    return students[student_id]

#query parameter
@app.get("/getbyname")
def get_data(name: str):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

#query and path parameter
@app.get("/getboth/{student_id}")
def get_data(student_id: int, name: str):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}