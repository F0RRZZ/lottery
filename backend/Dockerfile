FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements/prod.txt

CMD ["fastapi", "run", "src/main.py", "--proxy-headers", "--port", "8000", "--workers", "4"]
