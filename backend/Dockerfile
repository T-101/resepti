FROM python:3.11.1-alpine3.17

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apk update \
    && apk add gcc python3-dev musl-dev \
    && apk add nano bash htop \
    && apk add zlib-dev jpeg-dev
ENV TZ=Europe/Helsinki

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY .bashrc /root/

ADD . /app
