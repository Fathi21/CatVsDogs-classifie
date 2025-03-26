import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import matplotlib.pyplot as plt

# Constants
INPUT_SHAPE = (128, 128, 3)
NUM_CLASSES = 1
BATCH_SIZE = 32
EPOCHS = 50

# Step 1: Build the Model
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=INPUT_SHAPE),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(256, (3, 3), activation='relu'),  # Extra layer
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(NUM_CLASSES, activation='sigmoid')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.00005),
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
        shear_range=0.2,
        zoom_range=0.3,
        horizontal_flip=True,
        brightness_range=[0.7, 1.3]
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

# Step 3: Calculate Class Weights
def calculate_class_weights(train_generator):
    from sklearn.utils.class_weight import compute_class_weight
    import numpy as np
    
    labels = train_generator.classes
    class_weights = compute_class_weight('balanced', classes=np.unique(labels), y=labels)
    return dict(enumerate(class_weights))

# Step 4: Train the Model
def train_model(model, train_generator, val_generator):
    class_weights = calculate_class_weights(train_generator)

    callbacks = [
        EarlyStopping(monitor='val_loss', patience=7, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5)
    ]

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=val_generator,
        validation_steps=val_generator.samples // BATCH_SIZE,
        class_weight=class_weights,
        callbacks=callbacks
    )

    return history

# Step 5: Save the Model
def save_model(model):
    model.save('ML/cat_dog_classifier_v.h5')
    print("Model saved as 'ML/cat_dog_classifier_v.h5'")

# Step 6: Plot Training Results
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
