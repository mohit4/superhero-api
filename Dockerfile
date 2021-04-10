FROM python:3

MAINTAINER "Mohit Kumar"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:${PORT}