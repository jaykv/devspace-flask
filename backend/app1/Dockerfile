# this serves as the deployment image
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . .

EXPOSE 8080

CMD ["python", "main.py"]
