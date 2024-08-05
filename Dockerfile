# Use the official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y libhdf5-dev pkg-config gcc

# Upgrade pip and install setuptools and wheel
RUN pip install --upgrade pip setuptools wheel

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ /app/

# Expose the port on which the Flask app will run
EXPOSE 80

# Set environment variable for Flask
ENV FLASK_APP=deploy.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]