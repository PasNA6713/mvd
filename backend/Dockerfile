FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip setuptools

WORKDIR /usr/src/project

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install Cython
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/project

ENV SECRET_KEY="2312heuh2huU@GB2bwjhDUYWAgyEG^@GEhabIU@GHeahjbsdhjqb2cxz@eas43tyt54O*9njdsa"
ENV DB_NAME="postgres"
ENV DB_USER="postgres"
ENV DB_PASSWORD="postgres"
ENV DB_HOST="postgres"
ENV DB_PORT=5432

ENV REDIS_HOST="redis"

ENV DOCKER=True