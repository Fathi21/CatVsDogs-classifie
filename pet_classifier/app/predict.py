import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

class CatDogClassifier:
    def __init__(self, model_path, confidence_threshold):
        self.model = tf.keras.models.load_model(model_path)
        self.confidence_threshold = confidence_threshold

    def predict(self, img_path):
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(128, 128))  # Match the input size used during training
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize the image

        # Make a prediction
        prediction = self.model.predict(img_array)
        confidence = prediction[0][0]

        if confidence > 0.5:
            label = "Dog"
        else:
            label = "Cat"

        if confidence > 0.5:
            confidence = confidence
        else:
            confidence = 1 - confidence 

        # Apply the confidence threshold
        if confidence < self.confidence_threshold:
            label = "Unknown"
        # Format the confidence as a percentage
        confidence_percentage = confidence * 100
        return label, confidence_percentage