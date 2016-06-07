# Third party libs
from flask import Blueprint
from flask import render_template

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')

