from fastapi.confguration import Configuration

config = Configuration.load_config("config.prod.yaml")

class Envs:
    APP_NAME=config('DEBUG', default="API TCHAT")

    DB_HOST='127.0.0.1'
    DB_PORT='28025'
    DB_USER='root'
    DB_PASSWORD='root'
    DB_NAME='genikuiz'