# Third party libs
from flask import Flask
from flask.ext import cache_bust
from flask.ext.compress import Compress

# Blueprints
from .blueprints import root

def create_app(config_object):
    app = Flask(__name__, static_folder='../client/static')
    app.config.from_object(config_object)

    # Blueprints
    app.register_blueprint(root.blueprint)

    # Cache busting
    cache_bust.init_cache_busting(app)

    # Gzip compression
    Compress(app)

    return app

