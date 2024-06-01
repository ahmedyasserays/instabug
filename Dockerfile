FROM python:3.12-alpine
WORKDIR /instabug

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
