IMAGE_NAME := fashion-mnist-trainer
CONTAINER_NAME := $(IMAGE_NAME)

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) -f Dockerfile .

# Train the model using the Docker container
train-model: build
	@IMAGE_HASH=$$(docker images --format '{{.ID}}' $(IMAGE_NAME) | head -n 1) && \
	docker run --name $(CONTAINER_NAME) \
		-v $(pwd)/output:/app/output \
		-v $(pwd)/data:/app/data \
		--env-file .env \
		$$IMAGE_HASH

	# Move the trained model from the container to the host
	mv $(pwd)/output/fashion_mnist_model.h5 $(pwd)/model
	scp -i "iac/dbc_key" $(pwd)/model/fashion_mnist_model_final.h5 ec2-user@ec2-54-91-116-13.compute-1.amazonaws.com:~/.
