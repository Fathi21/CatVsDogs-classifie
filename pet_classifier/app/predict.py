import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

class CatDogClassifier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, img_path):
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(128, 128))  # Match the input size used during training
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize the image

        # Make a prediction
        prediction = self.model.predict(img_array)
        return "Dog" if prediction[0][0] > 0.5 else "Cat"