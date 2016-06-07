# Third party libs
from flask import Flask

# Blueprints
from .blueprints import root

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(root.blueprint)

    return app

