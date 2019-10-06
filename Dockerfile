FROM python:3.7-slim

ENV TZ Europe/Moscow
ENV PYTHONDONTWRITEBYTECODE yes

RUN mkdir /app
ENV HOME=/app
ENV PYTHONPATH=$HOME
WORKDIR $HOME

COPY configurations/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY configurations/config.py .
COPY sip_api $HOME/sip_api
