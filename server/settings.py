# Standard libs
import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

    WEBPACK_DEV_SERVER_HOSTNAME = os.getenv('WEBPACK_DEV_SERVER_HOSTNAME', 'localhost:8080')

    ITEMS_FILE = 'server/items.yaml'

