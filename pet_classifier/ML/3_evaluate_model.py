import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input

# Define the relative path to the model
model_path = os.path.join(os.path.dirname(__file__), 'Model', 'cat_dog_classifier.h5')

# Check if the file exists
if os.path.exists(model_path):
    print(f"File found: {model_path}")
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
else:
    print(f"File not found: {model_path}")
    exit()

