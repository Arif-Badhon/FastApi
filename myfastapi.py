#!/usr/bin/env python3
#import all
from optparse import Option
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
import uvicorn

#start fastapi
app = FastAPI()

#Dummy Data
students = {
    1 : {
        "Name":"Badhon",
        "age": 28,
        "designation": "Data Specialist"
    },
    2 : {
        "Name" : "Maha",
        "age" : 27,
        "designation" : "Market and Economic Specialist"
    },
    3 : {
        "Name" : "Sajid",
        "age" : 44,
        "designation" : "Luiccha"
    }
}

#class for adding new data

class Student(BaseModel):
    Name: str
    age: int
    designation: str

#class for updating

class UpdateStudent(BaseModel):
    Name: Optional[str] = None
    age: Optional[int] = None
    designation: Optional[str] = None

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

#request body and post method add new data
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:Student):
    if student_id in students:
        return {"Error": "Already exists"}
    
    students[student_id] = student
    return students[student_id]

#Update the student parameter
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.Name != None:
        students[student_id].Name = student.Name
    if student.age != None:
        students[student_id].age = student.age
    if student.designation != None:
        students[student_id].designation = student.designation
    return students[student_id]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)