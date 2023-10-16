import requests


url = "http://172.28.58.77:9696/predict"

customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=customer).json()

print(response)