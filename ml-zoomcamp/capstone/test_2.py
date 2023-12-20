import requests

def test_predict():
    url = 'http://127.0.0.1:5000/predict'
    image_url = 'https://raw.githubusercontent.com/cacaprog/learning-projects/main/ml-zoomcamp/row-1-column-4.jpg' 

    data = {'url': image_url}
    response = requests.post(url, json=data)

    print('Status Code:', response.status_code)
    print('Response:', response.text)

if __name__ == '__main__':
    test_predict()
