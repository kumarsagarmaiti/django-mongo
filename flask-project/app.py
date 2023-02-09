from flask import Flask, request
from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

from .employee_model import Employee

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
employee_collection = db["employees"]


@app.route("/")
def home():
    return "Hello World"


@app.route("/register", methods=["POST"])
def add_employee():
    employee = Employee.from_json(request.data)
    employee_collection.insert_one(employee.__dict__)
    return "success"


@app.route("/employees", methods=["GET"])
def get_all_employees():
    employees = employee_collection.find({})
    return json.loads(dumps(employees))


@app.route("/employee/<objectid>", methods=["GET", "PUT", "DELETE"])
def employee_by_id(objectid):
    find_by_id = {"_id": ObjectId(request.view_args["objectid"])}
    employee = employee_collection.find_one(find_by_id)
    if employee is None:
        return "Employee not found"
    if request.method == "GET":
        return json.loads(dumps(employee))

    if request.method == "PUT":
        employee_collection.update_one(find_by_id, {"$set": request.get_json()})
        return "Employee updated successfully"

    if request.method == "DELETE":
        employee_collection.delete_one(find_by_id)
        return "Employee deleted successfully"


if __name__ == "_main_":
    app.run(debug=True)
