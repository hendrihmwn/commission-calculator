prepare:
	pip install -r requirements.txt
	cd frontend && npm install
	cd frontend && npm run build

test:
	pytest

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

up:
	docker-compose up