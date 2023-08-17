# Local Development

### Build and run docker
1. `cp .env.local.example .env.local`
1. `cp .env.dev.example .env.dev`
1. `docker compose up -d --build`

### Run migration
`docker compose exec app alembic upgrade head`

### Upload data from excel-file
`docker compose exec app python manage.py load-from-xlsx posts.xlsx`

### Run in browser
http://127.0.0.1:8000/docs


## Migrations
- Create an automatic migration from changes in `src/database.py`
```shell
docker compose exec app alembic revision -m "<you_comment>" --autogenerate
```
- Run migrations
```shell
docker compose exec app alembic upgrade head
```
_Note: The download takes a few minutes_


## Manage commands

### Clear DB
```shell
docker compose exec app python manage.py clear-db
```