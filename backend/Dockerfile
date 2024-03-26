FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-root

COPY . /backend/

RUN poetry run python src/manage.py makemigrations
RUN poetry run python src/manage.py migrate --no-input

EXPOSE 8000

CMD poetry run python src/manage.py makemigrations && \
    poetry run python src/manage.py migrate --no-input && \
    poetry run python src/manage.py runserver 0.0.0.0:8000
