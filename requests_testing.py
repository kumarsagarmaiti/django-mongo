import requests
from requests.exceptions import HTTPError

# POST request for registering employee:
employee_body = {
    "name": "Kumar",
    "age": 28,
    "company": "Abnero",
    "email": "email4@gmail.com",
    "password": "password",
}

url = "http://127.0.0.1:8000/register"
try:
    response = requests.post(url, json=employee_body)

    response.raise_for_status()
    print(response.json())
except HTTPError as http_err:
    if response.status_code == 400:
        print(response.json())
    print(f"HTTP error occurred: {http_err}")  # Python 3.6
except Exception as err:
    print(f"Other error occurred: {err}")  # Python 3.6
else:
    print("Success!")

# GET request for getting all employees
url = "http://127.0.0.1:8000/employees"
try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())
except HTTPError as http_err:
    print(response.json())
else:
    print("Success")

# GET request for one employee
url = "http://127.0.0.1:8000/employee/32"

try:
    response = requests.get(
        url, headers={"email": "email4@gmail.com", "password": "password"}
    )
    response.raise_for_status()
    print(response.json())
except HTTPError as http_err:
    print(response.json())
