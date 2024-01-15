from decouple import config

class Envs:
    APP_NAME=config('DEBUG', default="API TCHAT")

    DB_HOST='195.110.34.74'
    DB_PORT='28025'
    DB_USER='root'
    DB_PASSWORD='root'
    DB_NAME='genikuiz'