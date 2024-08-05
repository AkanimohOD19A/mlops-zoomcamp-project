import os
import numpy as np
import random
import matplotlib.pyplot as plt
import mlflow
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient


# Load Fashion MNIST data
def load_fashion_mnist_data():
    (X_train, y_train), (X_val, y_val) = fashion_mnist.load_data()
    # Preprocess data
    X_train = np.expand_dims(X_train, axis=-1) / 255.0
    X_val = np.expand_dims(X_val, axis=-1) / 255.0
    return X_train, y_train, X_val, y_val


# Load data
X_train, y_train, X_val, y_val = load_fashion_mnist_data()


# Set up MLflow
TRACKING_SERVER_HOST = os.getenv("MLFLOW_HOST")
mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")

print(f"tracking URI: '{mlflow.get_tracking_uri()}'")

# Encode labels to integers
label_encoder = {i: label for i, label in enumerate(['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'])}
y_train = to_categorical(y_train, num_classes=10)
y_val = to_categorical(y_val, num_classes=10)

mlflow.search_experiments()
mlflow.set_experiment("fashion-mnist-experiment")

with mlflow.start_run():

    # Define the CNN model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    # Train the model
    history = model.fit(
        X_train, y_train,
        epochs=30,
        batch_size=32,
        validation_data=(X_val, y_val)
    )

    # Evaluate the model on the validation set
    val_loss, val_accuracy = model.evaluate(X_val, y_val)
    mlflow.log_metric("accuracy", val_accuracy)

    # Save the model
    mlflow.keras.log_model(model, artifact_path="models")

    # Function to predict the class of a random image from the dataset
    def predict_random_image(model, X, y, label_encoder):
        idx = random.randint(0, len(X) - 1)
        plt.imshow(X[idx].reshape(28, 28), cmap='gray')
        plt.title('Actual: ' + label_encoder[np.argmax(y[idx])])
        plt.show()

        # Predict the class of the selected image
        y_pred = model.predict(X[idx].reshape(1, 28, 28, 1))
        print(f'Prediction probabilities: {y_pred}')

        # Get the predicted class
        predicted_class = label_encoder[np.argmax(y_pred)]
        print(f'Predicted class: {predicted_class}')

    # Save the model
    model.save('./output/fashion_mnist_model.h5')

    # Load the trained model
    model = load_model('./output/fashion_mnist_model.h5')

    # Predict for a random image
    predict_random_image(model, X_val, y_val, label_encoder)

mlflow.end_run()

print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")
