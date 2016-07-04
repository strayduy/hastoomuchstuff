# Third party libs
from flask import abort
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import sendgrid
from sendgrid.helpers.mail import Content
from sendgrid.helpers.mail import Email
from sendgrid.helpers.mail import Mail
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
        'claimed_items': session.get('claimed_items', {}),
    }

    return jsonify(**res)

@blueprint.route('/claim-item', methods=['post'])
def claim_item():
    item_id = request.form['item_id']
    item_name = request.form['item_name']
    username = request.form['username']
    comments = request.form.get('comments', '')

    if not item_id or not item_name or not username:
        abort(400)

    app_config = current_app.config
    api_key = app_config.get('SENDGRID_API_KEY', '')

    if not api_key:
        abort(500)

    sg = sendgrid.SendGridAPIClient(apikey=api_key)
    from_email = Email(app_config['FROM_EMAIL_ADDRESS'], username)
    to_email = Email(app_config['TO_EMAIL_ADDRESS'])
    subject = '[DIBS] on %s' % (item_name)
    content = Content('text/plain', comments)
    mail = Mail(from_email, subject, to_email, content)
    res = sg.client.mail.send.post(request_body=mail.get())

    claimed_items = session.get('claimed_items', {})
    claimed_items[item_id] = True
    session['claimed_items'] = claimed_items

    return ''

