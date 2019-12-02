FROM python:3.7.3-alpine

ARG SUPERUSER_USERNAME
ARG SUPERUSER_EMAIL
ARG SUPERUSER_PASSWORD

RUN pip3 install --no-cache pipenv

RUN addgroup -g 9999 -S appuser \
  && adduser -u 9999 -S appuser -G appuser

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN mkdir /app \
  && chown 9999:9999 /app

WORKDIR /app

COPY Pipfile* ./
RUN pipenv install --system --deploy

USER appuser

COPY src .

RUN ./manage.py collectstatic

RUN ./manage.py migrate

RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser( \
    '${SUPERUSER_USERNAME}', \
    '${SUPERUSER_EMAIL}', \
    '${SUPERUSER_PASSWORD}' \
  )" | python manage.py shell

CMD ["conf.wsgi", "-c"]
