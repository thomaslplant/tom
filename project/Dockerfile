FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV YOUR NAME=Thomas

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]