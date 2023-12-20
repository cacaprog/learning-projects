import requests

#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://n06i2rjuk0.execute-api.us-east-1.amazonaws.com/test/predict'

data = {'url': 'https://raw.githubusercontent.com/cacaprog/learning-projects/main/ml-zoomcamp/row-1-column-4.jpg'}

result = requests.post(url, json=data).json()
print(result)