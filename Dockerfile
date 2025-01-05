FROM python:3.9

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY . .
RUN apt-get update && apt-get install -y nodejs npm
RUN apt-get clean -y
RUN pip install --upgrade pip
RUN make prepare