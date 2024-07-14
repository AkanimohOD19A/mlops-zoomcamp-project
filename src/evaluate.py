# src/evaluate.py
import tensorflow as tf
from data_preprocessing import load_and_preprocess_data

def evaluate_model(train_filepath, test_filepath, model_path):
    _, _, X_test, y_test = load_and_preprocess_data(train_filepath, test_filepath)

    model = tf.keras.models.load_model(model_path)

    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy}")
    print(f"Test Loss: {test_loss}")

    return test_loss, test_accuracy
