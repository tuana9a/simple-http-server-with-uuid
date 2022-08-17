# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN python3 -m venv .venv

COPY requirements.txt .

RUN .venv/bin/pip3 install -r requirements.txt

COPY main.py .

CMD .venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080
