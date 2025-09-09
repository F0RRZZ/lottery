#!/bin/bash

echo "[...] Start project"

if [ ! -f .env ]; then
    cp .env.example .env
    echo "[✓] .env created from .env.example"
else
    echo "[!] .env already exists, skipping creation"
fi

docker volume create --name=lottery-database
docker compose -f docker-compose.yml up -d

echo "[✓] Project started on http://localhost:1337"
