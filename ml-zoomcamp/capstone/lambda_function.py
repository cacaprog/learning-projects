import numpy as np
import requests
from io import BytesIO
from tflite_runtime.interpreter import Interpreter
from PIL import Image

# Function to load and preprocess the image
def load_preprocess_image(img_url, target_size=(224, 224)):
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content)).resize(target_size)
    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    # Normalize the image
    img_array /= 255.0
    return img_array


# Load the TensorFlow Lite model
interpreter = Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

# Get input and output tensors information
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# url = 'http://bit.ly/mlbookcamp-pants'


def predict(url):
    input_data = load_preprocess_image(url)
    
    # Check if input type is quantized, then rescale input data to uint8
    if input_details[0]['dtype'] == np.uint8:
        input_scale, input_zero_point = input_details[0]["quantization"]
        input_data = input_data / input_scale + input_zero_point

    # Set the tensor to point to the input data to be inferred
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run the inference
    interpreter.invoke()
    
    # Retrieve the model's output and post-process it as necessary
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)

    predicted_class = (output_data > 0.5).astype(int)
    if predicted_class[0][0] == 0:
        print("The person is wearing glasses.")
    else:
        print("The person is not wearing glasses.")

    # return predicted_class

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result