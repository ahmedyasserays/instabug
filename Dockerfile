FROM python:3.12-alpine
WORKDIR /instabug

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

ENV DATABASE_URL=sqlite:///db.sqlite3
ENV ALLOWED_HOSTS=127.0.0.1
ENV DEBUG=True

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

EXPOSE 4000
