FROM python:3.6-slim

COPY requirements.txt ./

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR /code

COPY . .

CMD ["python", "main.py"]
