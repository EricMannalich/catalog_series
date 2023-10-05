FROM python:3.11

ENV PYTHONUNBUFFERED=1
RUN mkdir /code/
WORKDIR /code
COPY . /code/

#Para poder instalar sycopg2 en python:alpine es necesario: 
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt