# Standard libs
import os

class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')

    ITEMS_FILE = 'server/items.yaml'

    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', '')
    FROM_EMAIL_ADDRESS = os.getenv('FROM_EMAIL_ADDRESS', '')
    TO_EMAIL_ADDRESS = os.getenv('TO_EMAIL_ADDRESS', '')

class ProdConfig(Config):
    APP_ENV = 'prod'

class DevConfig(Config):
    APP_ENV = 'dev'

    DEBUG = True

    WEBPACK_DEV_SERVER_HOSTNAME = os.getenv('WEBPACK_DEV_SERVER_HOSTNAME', 'localhost:8080')

