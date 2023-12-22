## Project Overview

### Dataset
**Glasses Classification Dataset from Kaggle**

This dataset includes a wide variety of eyeglasses images, offering a rich source for training machine learning models in classifying different types and styles of eyeglasses.

### Problem Statement
In 2023, an estimated 4 billion people globally wear glasses, highlighting their importance in daily life. Our project focuses on developing a model that can accurately identify if a person is wearing glasses. This is particularly relevant for facial recognition systems in diverse, populous areas like São Paulo, where the presence of eyeglasses can significantly alter facial recognition.

### Model Description
We use a Convolutional Neural Network (CNN) with ResNet architecture for this binary classification task. The model distinguishes between two classes: '0' for presence and '1' for absence of glasses.

## Local Setup and Testing Instructions

### Running Locally

1. **Clone the Repository**
   - `git clone https://github.com/cacaprog/learning-projects/tree/main/ml-zoomcamp/capstone`

2. **Set Up Environment**
   - Create a virtual environment using Pipenv and install dependencies from the provided Pipfile.

3. **Train the Model**
   - Run `python train.py` to train the model and save it as `resnet_model.H5`.

4. **Convert Model to TensorFlow Lite Format**
   - Execute `python converter.py` to convert the H5 model to a TensorFlow Lite model, saved as `resnet.tflite`.

5. **Run Prediction Script**
   - Launch the prediction script with `python predict.py`.

6. **Test the Model**
   - In a separate terminal, execute `python test_2.py` to test the model on a specified image.

### Running with Docker and Testing with Postman

#### Docker Setup

1. **Pull the Docker Image**
   - Run `docker pull cacaprog/glassesapp:dev`.

2. **Run the Docker Image**
   - Execute `docker run -p 5000:5000 glassesapp:dev`.
   - The application is accessible at `http://localhost:5000`.

#### Testing with Postman

1. **Install and Open Postman**
   - Download Postman from [here](https://www.postman.com/downloads/). Create an account and install the Postman agent for localhost testing.

2. **Create a New Request**
   - Click `+` or `Create New` to initiate a new request.

3. **Configure the Request**
   - Choose `POST` and enter `http://localhost:5000/predict`.

4. **Set Request Headers**
   - In the "Headers" tab, add `Content-Type` as `application/json`.

5. **Add JSON Body**
   - Switch to the "Body" tab, select `raw` and `JSON`.
   - Input your JSON data, for example:
     `{ "url": "https://raw.githubusercontent.com/cacaprog/learning-projects/main/ml-zoomcamp/row-1-column-4.jpg" }`

6. **Send and View the Response**
   - Click `Send`. The server's response, including status code and response body, will be displayed in Postman.


### Testing with ECR Lambda

1. **Access the AWS Lambda Function**
   - Use the provided AWS Lambda endpoint: https://n06i2rjuk0.execute-api.us-east-1.amazonaws.com/test.
        This endpoint is configured to interact with the Glasses Classification Model.

2. **Run the Test Script**
   - Execute the test.py file locally.
        This script is designed to send a request to the AWS Lambda function and receive the classification results.
