import os

# Define the path to the directory containing the model
directory_path = './CatVsDogs-classifie/pet_classifier/app/Model/cat_dog_classifier.h5'

# List the contents of the directory

files = os.listdir(directory_path)
print(f"Files in '{files}':")

