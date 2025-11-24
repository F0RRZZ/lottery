FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements/prod.txt

CMD ["taskiq", "worker", "src.task_app:broker", "--fs-discover"]
