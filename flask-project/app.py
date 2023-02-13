import json

from bson.json_util import dumps
from bson.objectid import ObjectId
from dataclass_wizard.errors import MissingFields
from flask import Flask, request, abort, Response, jsonify
from pymongo import MongoClient

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
    try:
        employee = Employee.from_json(request.data)
        employee_collection.insert_one(employee.__dict__)
        return "success"
    except MissingFields as e:
        return Response(f"Missing field: {e.missing_fields}", status=400)
    except Exception as e:
        return Response(f"An error occured {e}")


@app.route("/employees", methods=["GET"])
def get_all_employees():
    query = request.args.to_dict()
    body = request.get_json()
    try:
        if body is not None:
            body["_id"] = 0
            employees = employee_collection.find({}, body)
        if "groupBy" in query:
            pipeline = [
                {
                    "$group": {
                        "_id": f"${query.get('groupBy')}",
                        "name": {"$push": "$name"},
                    }
                }
            ]
            employees = employee_collection.aggregate(pipeline)
        else:
            if "age" in query:
                query["age"] = int(query["age"])
            employees = employee_collection.find(query, {"_id": 0})
        return list(employees)
    except Exception as e:
        return Response(f"An error occured {e}")


@app.route("/employee/<objectid>", methods=["GET", "PUT", "DELETE"])
def employee_by_id(objectid):
    try:
        find_by_id = {"_id": ObjectId(objectid)}
        employee = employee_collection.find_one(find_by_id)
        if employee is None:
            abort(code=404)
        if request.method == "GET":
            return json.loads(dumps(employee))

        if request.method == "PUT":
            employee_collection.update_one(find_by_id, {"$set": request.get_json()})
            return "Employee updated successfully"

        if request.method == "DELETE":
            employee_collection.delete_one(find_by_id)
            return "Employee deleted successfully"
    except Exception as e:
        return Response(f"An error occured {e}")


if __name__ == "_main_":
    app.run(debug=True)
