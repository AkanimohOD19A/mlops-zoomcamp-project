# src/data_preprocessing.py
import numpy as np
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(train_filepath, test_filepath):
    train = pd.read_csv(train_filepath)
    test = pd.read_csv(test_filepath)

    X_train = (train.iloc[:, 1:].values) / 255.0  # Normalize pixel values
    y_train = train["label"].values

    X_test = (test.iloc[:, 1:].values) / 255.0    # Normalize pixel values
    y_test = test["label"].values

    # Reshape X_train and X_test for CNN input
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    return X_train, y_train, X_test, y_test
