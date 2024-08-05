# Fashion MNIST Image Classifier

![alt text](intro.png "Fashion MNIST Classifier")

## Problem Definition
This project aims to develop a Flask-based web application that classifies fashion items into specific categories using a convolutional neural network (CNN) model. The project will also employ MLOps techniques to ensure the application is robust and maintainable. This includes continuous integration, continuous deployment (CI/CD), automated testing, and containerization.

## Dataset Overview
Fashion-MNIST is a dataset developed by Zalando, consisting of 70,000 grayscale images of fashion items. It serves as a benchmark for machine learning algorithms, designed to replace the original MNIST dataset while maintaining the same format and size.

### Dataset Details
- **Size and Structure**: The dataset comprises a training set of 60,000 examples and a test set of 10,000 examples. Each image is 28x28 pixels, resulting in a total of 784 pixels per image.
- **Labeling**: Images are associated with 10 distinct classes representing different fashion items:
  - 0: T-shirt/top
  - 1: Trouser
  - 2: Pullover
  - 3: Dress
  - 4: Coat
  - 5: Sandal
  - 6: Shirt
  - 7: Sneaker
  - 8: Bag
  - 9: Ankle boot
- **Pixel Values**: Each pixel in the image has an integer value ranging from 0 to 255, representing its lightness or darkness.

### Content Description
- **Data Format**: Both the training and test datasets are structured with 785 columns. The first column contains the class label, while the remaining 784 columns correspond to the pixel values of the associated image.
- **Image Preprocessing**: Pixel values are normalized to a range of 0 to 1 by dividing each value by 255.

## Objective
The goal of this project is to develop a convolutional neural network (CNN) model capable of accurately classifying these fashion items based on their grayscale images. The model will be trained on the training dataset and evaluated on the test dataset to measure its performance in terms of accuracy and loss.

## Approach
1. **Data Loading and Preprocessing**: Load the dataset, preprocess the images by normalizing pixel values, and split them into training and testing sets.
2. **Model Development**: Construct a CNN model using TensorFlow/Keras to classify the fashion items. Experiment with different architectures and hyperparameters to optimize model performance.
3. **Training and Evaluation**: Train the model on the training set, monitor its performance using validation data, and evaluate it on the test set to assess generalization capability.
4. **Deployment**: Deploy the trained model as a web application using Flask, allowing users to upload images for real-time classification.

## MLOps Practices
- **Code Quality**: Utilize linting tools (e.g., flake8) to maintain high code quality.
- **Automated Testing**: Implement unit and integration tests using pytest to ensure the application works as expected.
- **Continuous Integration**: Set up GitHub Actions to automate testing and linting on each commit.
- **Containerization**: Use Docker to containerize the application for consistent deployment across different environments.
- **Makefile Automation**: Create a Makefile to automate common tasks like building and running the Docker container, running tests, and linting.

## Infrastructure Setup
### Generate EC2 instance SSH key
```bash
cd iac && ssh-keygen -f fashion_mnist_key
