import tensorflow as tf

# Load the H5 model
model = tf.keras.models.load_model('resnet_model.h5')

# Convert the model to the TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open('resnet.tflite', 'wb') as f:
    f.write(tflite_model)