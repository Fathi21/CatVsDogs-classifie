# Need to read the PetImage folder 
# check if any bad images in the folder "PetImage"  
# sprate the data into:
# training data 
# test data 
# validation data 

import os
import shutil
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split

os.chdir("pet_classifier/ML")

# Constants
INPUT_FOLDER = "PetImages"  # Folder containing cat/dog subfolders
OUTPUT_FOLDER = os.path.join("dataset")  # Output folder inside existing ML folder
TRAIN_RATIO = 0.7           # 70% training data
VAL_RATIO = 0.15            # 15% validation data
TEST_RATIO = 0.15           # 15% test data
SEED = 42                   # For reproducibility

# Create output folders
os.makedirs(os.path.join(OUTPUT_FOLDER, "Train/cats"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "Train/dogs"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "Validation/cats"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "Validation/dogs"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "Test/cats"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "Test/dogs"), exist_ok=True)