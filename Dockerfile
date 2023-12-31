FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code/
WORKDIR /code
COPY . /code/
#RUN git clone https://github.com/EricMannalich/catalog_series.git
#WORKDIR /catalog_series

RUN apt update
#RUN apt upgrade
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt