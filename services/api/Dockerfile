FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./core ./core
COPY ./db ./db
COPY ./schemas ./schemas
COPY ./routers ./routers
COPY ./services ./services

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]