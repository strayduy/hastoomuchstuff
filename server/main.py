#!python2.7

# Standard libs
import os

# Our libs
from .app import create_app
from .settings import Config

app = create_app(Config)

