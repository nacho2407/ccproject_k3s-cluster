FROM python:3.13-slim

RUN apt update && apt upgrade -y && apt-get install -y gcc stress curl && apt-get clean

RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py /app/main.py

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
