FROM python:3.11-slim
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5
WORKDIR /app
COPY environment/access.log /app/access.log
COPY solution /app/solution
COPY tests /app/tests