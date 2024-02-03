FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY requirements.txt /backend/

RUN apt install pkg-config \
    && pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

COPY . .


# django 서버 gunicorn 이용해 실행
# CMD [ "gunicorn", "--config", "gunicorn_config.py", "app.wsgi:application" ]