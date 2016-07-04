# Standard libs
import os

class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

    ITEMS_FILE = 'server/items.yaml'

class ProdConfig(object):
    APP_ENV = 'prod'

class DevConfig(object):
    APP_ENV = 'dev'

    DEBUG = True

    WEBPACK_DEV_SERVER_HOSTNAME = os.getenv('WEBPACK_DEV_SERVER_HOSTNAME', 'localhost:8080')

