from decouple import config

class Envs:
    APP_NAME=config('DEBUG', default="API TCHAT")

    DB_HOST=config('DB_HOST')
    DB_PORT=config('DB_PORT')
    DB_USER=config('DB_USER')
    DB_PASSWORD=config('DB_PASSWORD')
    DB_NAME=config('DB_NAME')