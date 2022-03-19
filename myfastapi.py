#import all
from fastapi import FastAPI, Path
from pydantic import BaseModel

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

#class for adding new data

class Student(BaseModel):
    Name: str
    age: int
    designation: str

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

#request body and post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:Student):
    if student_id in students:
        return {"Error": "Already exists"}
    
    students[student_id] = student
    return students[student_id]
    