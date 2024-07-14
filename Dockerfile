# Use the official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies
RUN pip install -r requirements.txt

# Copy model and deployment scripts
COPY fashion_mnist_model.h5 /
COPY deploy.py /

# Set the working directory
WORKDIR /

# Run deployment script
CMD ["python", "deploy.py"]
