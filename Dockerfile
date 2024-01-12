FROM python:3.9

WORKDIR /usr/src/app

WORKDIR /app


ENV PYTHONDONTWRITTERBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .