FROM python:3.9-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6

RUN apt-get update && apt-get --no-install-recommends install -y build-essential git openssh-client

RUN pip install --upgrade pip
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev --no-interaction --no-ansi

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./docker/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./docker/gunicorn.conf.py /gunicorn.conf.py

COPY ./app /app/app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["/start.sh"]

ARG VCS_REF
ARG BUILD_DATE
ARG TAG_NAME

ENV RELEASE=$TAG_NAME

LABEL vcs_ref=$VCS_REF \
      build_date=$BUILD_DATE \
      release=$RELEASE \
      project="test-hash" \
      application="test-task-hash" \
      maintainer="gleb.m.k."
