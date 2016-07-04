# Third party libs
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import render_template
from flask import url_for
import yaml

# Initialize blueprint
blueprint = Blueprint('root', __name__)

@blueprint.route('/')
def index():
    app_config = current_app.config
    env = app_config.get('APP_ENV', 'dev').lower()
    webpack_dev_server_hostname = app_config.get('WEBPACK_DEV_SERVER_HOSTNAME', '')

    unminified_filename = 'app/js/index.bundle.js'
    minified_filename = 'app/js/index.bundle.min.js'

    if env == 'prod':
        bundle_url = url_for('static', filename=minified_filename)
    elif webpack_dev_server_hostname:
        # Not using url_for to avoid creating a cachebusted URL
        bundle_url = 'http://%s/static/%s' % (webpack_dev_server_hostname, unminified_filename)
    else:
        bundle_url = url_for('static', filename=unminified_filename)

    template_vars = {
        'bundle_url': bundle_url,
    }

    return render_template('index.html', **template_vars)

@blueprint.route('/items.json')
def items():
    app_config = current_app.config
    with open(app_config['ITEMS_FILE']) as f:
        item_data = yaml.safe_load(f)

    res = {
        'items': item_data['items'],
    }

    return jsonify(**res)

