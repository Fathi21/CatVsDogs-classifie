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
INPUT_FOLDER = os.path.join("PetImages")  # Folder containing cat/dog subfolders
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

def clean_corrupt_files(folder_path):
    """
    Remove corrupt or non-image files from a folder.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Open and verify the image
                with Image.open(file_path) as img:
                    img.verify()  # Verify integrity
                    img = Image.open(file_path)  # Reopen to check loading
                    img.close()
            except (IOError, SyntaxError, Image.UnidentifiedImageError, Exception) as e:
                print(f"Removing corrupt file: {file_path} (Error: {e})")
                os.remove(file_path)
def split_data(class_name):
    """
    Split data for a specific class (cats or dogs) into train/val/test sets.
    """
    # Get list of files
    class_dir = os.path.join(INPUT_FOLDER, class_name)
    files = [os.path.join(class_dir, f) for f in os.listdir(class_dir)]

    # Split into train/val/test
    train_files, temp_files = train_test_split(files, test_size=(1 - TRAIN_RATIO), random_state=SEED)
    val_files, test_files = train_test_split(temp_files, test_size=TEST_RATIO/(TEST_RATIO + VAL_RATIO), random_state=SEED)

    # Copy files to target folders
    def copy_files(files, target_dir):
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            shutil.copy(f, target_dir)

    copy_files(train_files, os.path.join(OUTPUT_FOLDER, "train", class_name))
    copy_files(val_files, os.path.join(OUTPUT_FOLDER, "validation", class_name))
    copy_files(test_files, os.path.join(OUTPUT_FOLDER, "test", class_name))

def main():
    # Step 1: Clean corrupt files in the input folder
    print("Cleaning corrupt files...")
    clean_corrupt_files(INPUT_FOLDER)

    # Step 2: Split data for cats and dogs
    print("Splitting data into train/val/test sets...")
    split_data("Cat")
    split_data("Dog")

    print(f"Data organisation complete! Check the '{OUTPUT_FOLDER}' folder.")

if __name__ == "__main__":
    main()