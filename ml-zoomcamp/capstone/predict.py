from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import requests
from io import BytesIO

app = Flask(__name__)

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="resnet.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def model_predict(img_url):
    response = requests.get(img_url)
    img = tf.keras.preprocessing.image.load_img(BytesIO(response.content), target_size=(150, 150))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    interpreter.set_tensor(input_details[0]['index'], x)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_details[0]['index'])

    return preds

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    if 'url' not in data:
        return "JSON must contain the 'url' key", 400

    img_url = data['url']
    
    # Make prediction
    preds = model_predict(img_url)

    # Process your result
    pred_class = preds.argmax(axis=-1)[0] # Simple argmax for binary classification
    if pred_class == 0:
        message = "The person is wearing glasses."
    else:
        message = "The person is not wearing glasses."
    return jsonify({"prediction": message})
    
    #result = str(pred_class[0])
    #return result 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
