import requests

url = 'http://172.28.58.77:9696/predict'

customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=customer).json()

print(response)