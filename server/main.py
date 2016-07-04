#!python2.7

# Standard libs
import os

# Our libs
from .app import create_app
from .settings import DevConfig
from .settings import ProdConfig

env = os.getenv('APP_ENV', 'dev')
config_class = ProdConfig if env == 'prod' else DevConfig
app = create_app(config_class)

