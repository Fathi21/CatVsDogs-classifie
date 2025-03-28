import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers
import matplotlib.pyplot as plt

# Constants
INPUT_SHAPE = (128, 128, 3)
NUM_CLASSES = 1
BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 1e-5

# Step 1: Build the Model
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=INPUT_SHAPE, kernel_regularizer=regularizers.l2(0.001)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Conv2D(64, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.001)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Conv2D(128, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.001)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Flatten(),
        Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
        Dropout(0.5),
        Dense(NUM_CLASSES, activation='sigmoid')
    ])

    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model

# Step 2: Prepare Data Generators
def prepare_data():
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True,
        brightness_range=[0.7, 1.3],
        channel_shift_range=30.0
    )

    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        '/Users/sharif/Desktop/projects/CatVsDogs-classifie/pet_classifier/ML/dataset/Train',
        target_size=INPUT_SHAPE[:2],
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    val_generator = val_datagen.flow_from_directory(
        '/Users/sharif/Desktop/projects/CatVsDogs-classifie/pet_classifier/ML/dataset/Validation',
        target_size=INPUT_SHAPE[:2],
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    return train_generator, val_generator

# Step 3: Train the Model
def train_model(model, train_generator, val_generator):
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=val_generator,
        validation_steps=val_generator.samples // BATCH_SIZE,
        callbacks=[early_stopping]
    )

    return history

# Step 4: Save the Model
def save_model(model):
    model.save('ML/improved_cat_dog_classifier.h5')
    print("Model saved as 'ML/improved_cat_dog_classifier.h5'")

# Step 5: Plot Training Results
def plot_results(history):
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Main Function
def main():
    print("Building the model...")
    model = build_model()
    model.summary()

    print("Preparing data generators...")
    train_generator, val_generator = prepare_data()

    print("Training the model...")
    history = train_model(model, train_generator, val_generator)

    print("Saving the model...")
    save_model(model)

    print("Plotting training results...")
    plot_results(history)

if __name__ == "__main__":
    main()
