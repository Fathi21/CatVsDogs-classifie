import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix


# Load the model
model_path = './pet_classifier/app/Model/cat_dog_classifier.h5'
model = tf.keras.models.load_model(model_path)

