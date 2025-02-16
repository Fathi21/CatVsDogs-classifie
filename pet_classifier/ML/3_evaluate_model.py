import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Define the relative path to the model (more robust)
model_dir = os.path.join(os.path.dirname(__file__), 'ML')  # Directory containing the model
model_path = os.path.join(model_dir, '2cat_dog_classifier.h5')

# Check if the model directory and file exists
if os.path.exists(model_dir) and os.path.exists(model_path):
    print(f"Model file found: {model_path}")
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
else:
    if not os.path.exists(model_dir):
        print(f"Error: Model directory not found: {model_dir}")
    else:
        print(f"Error: Model file not found: {model_path}")
    exit()

# Constants
INPUT_SHAPE = (128, 128, 3)
BATCH_SIZE = 32

# Step 1: Load and preprocess the test data
def load_test_data():
    # Corrected and more robust path to test data (relative path)
    test_dir = os.path.join(os.path.dirname(__file__), 'dataset', 'test')  # Simplified relative path

    if not os.path.exists(test_dir):
        print(f"Error: Test directory not found: {test_dir}")
        exit()

    test_datagen = ImageDataGenerator(rescale=1./255)  # Rescaling only

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=INPUT_SHAPE[:2],
        batch_size=BATCH_SIZE,
        class_mode='binary',  # Or 'categorical' if you have more than two classes
        shuffle=False
    )

    return test_generator

# Step 2: Evaluate the model
def evaluate_model(model, test_generator):
    print("Evaluating the model...")
    loss, accuracy = model.evaluate(test_generator, steps=len(test_generator))  # Use steps for correct evaluation
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    # Get predictions and true labels (more efficient)
    y_true = test_generator.classes
    y_pred_probabilities = model.predict(test_generator, steps=len(test_generator))
    y_pred = (y_pred_probabilities > 0.5).astype(int).flatten()  # Threshold probabilities for binary classification

    # Generate confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print("\nConfusion Matrix:")
    print(cm)

    # Plot confusion matrix with improved readability
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
                xticklabels=['Cat', 'Dog'], yticklabels=['Cat', 'Dog'],
                annot_kws={'size': 16})  # Increase annotation font size
    plt.xlabel('Predicted', fontsize=14)
    plt.ylabel('True', fontsize=14)
    plt.title('Confusion Matrix', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

    # Generate classification report
    print("\nClassification Report:")
    report = classification_report(y_true, y_pred, target_names=['Cat', 'Dog'], output_dict=True)
    print(classification_report(y_true, y_pred, target_names=['Cat', 'Dog']))

    # Plot metrics summary table
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    values = [accuracy, report['Cat']['precision'], report['Cat']['recall'], report['Cat']['f1-score']]

    plt.figure(figsize=(8, 4))
    plt.table(cellText=[values],
              colLabels=metrics,
              loc='center',
              cellLoc='center',
              colWidths=[0.2] * len(metrics))
    plt.axis('off')  # Hide axes
    plt.title('Model Evaluation Metrics', fontsize=16, pad=20)
    plt.show()

# Step 3: Main function
def main():
    print("Loading test data...")
    test_generator = load_test_data()

    evaluate_model(model, test_generator)

if __name__ == "__main__":
    main()