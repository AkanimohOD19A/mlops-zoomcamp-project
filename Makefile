install:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8 src/

format:
	black src/

run:
	python src/main.py

docker-build:
	docker build -t fashion-mnist .

docker-run:
	docker run -p 5000:5000 fashion-mnist
