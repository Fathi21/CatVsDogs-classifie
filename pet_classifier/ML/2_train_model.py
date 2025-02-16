import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Constants
INPUT_SHAPE = (128, 128, 3)  # Smaller image size
NUM_CLASSES = 1               # Binary classification (cat vs. dog)
BATCH_SIZE = 32               # Batch size
EPOCHS = 10                   # Number of training iterations

# Step 1: Build the Model
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=INPUT_SHAPE),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),  # Add dropout
        Dense(NUM_CLASSES, activation='sigmoid')
    ])

    # Compile the model
    model.compile(
        optimizer=Adam(learning_rate=0.0001),  # Lower learning rate
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model

# Step 2: Prepare Data Generators
def prepare_data():
    # Data augmentation and preprocessing for training data
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,  # Add shear
        zoom_range=0.2,
        horizontal_flip=True,
        brightness_range=[0.8, 1.2]  # Add brightness adjustment
    )

    # Only rescale for validation/test data
    val_datagen = ImageDataGenerator(rescale=1./255)

    # Load data from directories
    train_generator = train_datagen.flow_from_directory(
        '/workspaces/CatVsDogs-classifie/pet_classifier/ML/dataset/train',  # Absolute path
        target_size=INPUT_SHAPE[:2],  # Use smaller image size
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    val_generator = val_datagen.flow_from_directory(
        '/workspaces/CatVsDogs-classifie/pet_classifier/ML/dataset/validation',  # Absolute path
        target_size=INPUT_SHAPE[:2],  # Use smaller image size
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    return train_generator, val_generator

# Step 3: Train the Model
def train_model(model, train_generator, val_generator):
    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=val_generator,
        validation_steps=val_generator.samples // BATCH_SIZE
    )

    return history

# Step 4: Save the Model
def save_model(model):
    model.save('ML/cat_dog_classifier.h5')
    print("Model saved as 'ML/cat_dog_classifier.h5'")

# Step 5: Plot Training Results
def plot_results(history):
    # Plot training & validation accuracy
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Plot training & validation loss
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Main Function
def main():
    # Step 1: Build the model
    print("Building the model...")
    model = build_model()
    model.summary()

    # Step 2: Prepare data generators
    print("Preparing data generators...")
    train_generator, val_generator = prepare_data()

    # Step 3: Train the model
    print("Training the model...")
    history = train_model(model, train_generator, val_generator)

    # Step 4: Save the model
    print("Saving the model...")
    save_model(model)

    # Step 5: Plot training results
    print("Plotting training results...")
    plot_results(history)

if __name__ == "__main__":
    main()
