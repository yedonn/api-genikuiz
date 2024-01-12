FROM python:3.9

WORKDIR /usr/src/app

WORKDIR /app


ENV PYTHONDONTWRITTERBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]