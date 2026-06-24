FROM python:3.11-slim@sha256:e2219238da88a0b0aa9ba8a1a3e55cfcfd4049d2e8c31cc3e01efc3e4ea9dcc5

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log