import requests
import json

url = "http://second_container:5000/add_numbers"
data = {"a":2, "b":3}
response = requests.post(url, json=data)
result = response.json()["result"]

print(result)
