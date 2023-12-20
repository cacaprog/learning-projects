#!/usr/bin/env python
# coding: utf-8

# Importing necessary libraries
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.optimizers import Adam
import os

# Function to create the model
def create_model():
    resnet_model = ResNet50(weights='imagenet', 
                            include_top=False, 
                            input_shape=(150, 150, 3))

    x = resnet_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(1, activation='sigmoid')(x)  

    model = Model(inputs=resnet_model.input, outputs=predictions)

    return model

# Function to load and preprocess data
def load_data(train_dir, val_dir):
    train_datagen = ImageDataGenerator(rescale=1./255)
    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary',
        shuffle=True)

    val_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary',
        shuffle=True)

    return train_generator, val_generator


# Main function to train the model
def train_model():
    train_dir = 'data/glasses_dataset/train'
    val_dir = 'data/glasses_dataset/validate'

    train_generator, val_generator = load_data(train_dir, val_dir)

    model = create_model()
    
    # Freeze only the layers of the pre-trained model
    for layer in model.layers[:-3]:
        layer.trainable = False

    model.compile(optimizer=Adam(learning_rate=0.001), 
                  loss='binary_crossentropy', 
                  metrics=['accuracy'])
    
    history = model.fit(train_generator, 
                        validation_data=val_generator, 
                        epochs=10)

    # Save the model
    model.save('resnet_model.h5')

if __name__ == '__main__':
    train_model()