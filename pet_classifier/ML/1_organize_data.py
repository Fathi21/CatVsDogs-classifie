import os

def count_images_in_subfolders(folder_path):
    """
    Counts the number of image files (jpg, jpeg, png, gif, bmp) 
    in the "cats" and "dogs" subfolders of a given folder.

    Args:
        folder_path: The path to the main folder containing "cats" and "dogs" subfolders.

    Returns:
        A dictionary containing the counts for "cats" and "dogs", or 
        a string message if there's an issue with the folder structure.
        Returns an empty dictionary if no images are found.
    """

    try:
        cats_folder = os.path.join(folder_path, "Cat")
        dogs_folder = os.path.join(folder_path, "Dog")

        if not os.path.exists(cats_folder) or not os.path.exists(dogs_folder):
            return "Error: 'cats' or 'dogs' subfolders not found."

        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]  # Add more if needed.
        counts = {"cats": 0, "dogs": 0}

        for folder_name, folder_path in [("cats", cats_folder), ("dogs", dogs_folder)]:
            if os.path.exists(folder_path): #check if folder exists
                for filename in os.listdir(folder_path):
                    if any(filename.lower().endswith(ext) for ext in image_extensions):
                        counts[folder_name] += 1
        return counts

    except Exception as e:
        return f"An error occurred: {e}"



# Example usage:
folder_path = "/Users/sharif/Desktop/projects/CatVsDogs-classifie/pet_classifier/ML/PetImages"  # Replace with the actual path
image_counts = count_images_in_subfolders(folder_path)

if isinstance(image_counts, dict): #check if it's a dictionary
    if not image_counts: #check if it's an empty dictionary
        print("No images found in the specified folders.")
    else:
        print("Image counts:")
        for category, count in image_counts.items():
            print(f"{category}: {count}")
elif isinstance(image_counts, str): #check if it's a string (error message)
    print(image_counts) #print the error message