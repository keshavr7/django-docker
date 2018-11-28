# django-docker

Dockerised Django App with Postgres, Redis and Celery

## Setup

1) Create a .env in dj_root directory

Sample .env file. No API keys or tokens, safe to share :)
Feel free to change Postgres DB instance

    BROKER_CONNECTION_TIMEOUT=30
    BROKER_HEARTBEAT=30
    BROKER_POOL_LIMIT=1
    BROKER_URL=redis://redis:6379/0
    CELERY_EVENT_QUEUE_EXPIRE=60
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    CELERY_SEND_EVENTS=0
    DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
    DJANGO_SETTINGS_MODULE=www.settings.local_settings
    SECRET_KEY=%j##m!m75a*wkjo!1jsmc728)y7)o#5qm@qv(@)-@3zym-6lz)
    REDISCLOUD_URL=redis://redis:6379/0
    REDIS_BLOCKING_TIMEOUT=25
    REDIS_MAX_CONNECTIONS=3

2) Run docker-compose up -d

3) Visit http://0.0.0.0:8000
