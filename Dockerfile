# Image initial
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Port d'accès
EXPOSE 80

# Command d'exécution de notre app
CMD uvicorn app:app --host 0.0.0.0 --port $PORT