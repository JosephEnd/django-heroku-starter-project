FROM python:3.7.3

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY Pipfile* ./
RUN pip3 install --no-cache pipenv
RUN pipenv install --system --deploy --dev
