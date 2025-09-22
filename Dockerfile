FROM python:3.13-slim-bookworm
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    gcc \
    libxml2-dev \
    libxslt-dev \
    libxmlsec1-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

RUN mkdir /PawPrints

WORKDIR /PawPrints

ADD ./requirements.txt /PawPrints/requirements.txt
RUN pip install -r requirements.txt

ADD . /PawPrints

RUN python manage.py renderfiles && python manage.py compress
