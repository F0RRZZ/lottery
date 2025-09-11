<img src="assets/lottery-white.svg">

Хагажеев Марат, Конников Глеб, 23-КБ-ПР1


## Установка и запуск

Перед установкой и запуском программы необходимо установить следующее программное обеспечение:

* [Docker](https://www.docker.com/)
* Для Windows — [GitBash](https://gitforwindows.org/)

После установки ПО нужно проделать следующие шаги:

1. Склонируйте репозиторий

```bash
git clone https://github.com/F0RRZZ/lottery.git
```

2. Перейдите в директорию проекта

```bash
cd lottery
```

3. Запустите скрипт установки [first-run.sh](first-run.sh)
Скрипт автоматически создаст файл с переменными окружения .env и запустит проект с помощью Docker

```bash
chmod +x first-run.sh && ./first-run.sh
```

После проделывания всех шагов сайт будет доступен по локальной ссылке `http://localhost:1337`

Проект так же можно запустить вручную.

1. Создайте файл с переменными окружения .env. Создать файл вы можете опираясь на образец [.env.example](.env.example). Его можно скопировать и отредактировать по надобности

```bash
cp .env.example .env
```

2. Создайте volume для базы данных

```bash
docker volume create --name=lottery-database
```

3. Поднимите контейнеры в Docker

```bash
docker compose -f docker-compose.yml up -d
```

После этого проект также будет доступен по локальной ссылке `http://localhost:1337/`
