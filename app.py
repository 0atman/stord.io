"Code for stord.io, a REST wrapper around redis."
import os
from functools import wraps
import json
from uuid import uuid4
import datetime
import smtplib

from flask import (
    Response,
    redirect,
    Flask,
    request,
    flash,
    render_template,
)
from flask_restful import (
    Resource,
    Api,
    reqparse,
)
from flask_mail import (
    Mail,
    Message,
)
from redis import StrictRedis


app = Flask(__name__)
app.debug = True if os.getenv('FLASK:DEBUG', False) == 'True' else False
app.config['MAIL_SERVER'] = os.getenv('FLASK:EMAIL_HOST')
mail = Mail(app)
app.config['SECRET_KEY'] = 'unused'
r = StrictRedis(host='db', port=6379, db=0)
parser = reqparse.RequestParser()
parser.add_argument('auth')


def check_auth(auth):
    """
    This function is called to check if the auth code is in the db.
    """
    return bool(r.hget('auth', auth))


def authenticate():
    """
    Sends a 401 response that enables basic auth
    """

    return Response(
        'Could not verify your access level for that URL.\n'
        'Please provide valid auth token.', 401,
    )


def requires_auth(f):
    """
    Wrap functions that need auth token with this.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        args = parser.parse_args()
        auth = args.get('auth', False)
        if not auth or not check_auth(auth):
            return authenticate()
        return f(auth=auth, *args, **kwargs)
    return decorated


def generate_token(email):
    """
    Creates and returns a new auth token.
    """
    new_token = uuid4()
    r.hset('auth', new_token, "%s:%s" % (
        email,
        str(datetime.datetime.now())
    ))
    return new_token


@app.route('/')
def index():
    return redirect("http://www.stord.io", 301)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email'].strip()
        msg = Message(
            "Stord.io API key",
            sender="auth@stord.io",
            recipients=[email]
        )
        msg.body = "API Key"
        msg.html = render_template('email.html', key=generate_token(email))
        try:
            mail.send(msg)
            lobbyists = [
                'tristram@oaten.name',
                'karl@deadlight.net',
                'lewis@oaten.name',
                'danyilmaz117@gmail.com',
                'will@willmoggridge.com',
                'will.moggridge@gmail.com',
                'darkxdragon@gmail.com',
                'robin@robinwinslow.co.uk'
            ]
            if request.form['email'] in lobbyists:
                flash("Welcome #Lobbyist", 'info')
            flash('An API key has been sent to %s. Go check your email!' % (
                request.form['email'],
            ), 'success')
            flash("Not recieved your key? Check your spam folder!", 'info')
            mail.send(Message(
                "%s just registered!" % email,
                sender="auth@stord.io",
                recipients=['tristram@oaten.name']
            ))
        except smtplib.SMTPRecipientsRefused as e:
            flash('Bad email address: ' + e.args[0][email][1], 'danger')

    return render_template('signup.html')


api = Api(app)


class Store(Resource):
    @requires_auth
    def delete(self, key, auth):
        status = r.hget(auth, key)
        if status == 1:
            return {
                "deleted": "OK"
                } 
        else:
            return {
            'Not found': key
            }, 404

    @requires_auth
    def get(self, key, auth):
        value = r.hget(auth, key)
        if value is None:
            return {
                'Not found': key
            }, 404
        else:
            return {
                key: value
            }

    @requires_auth
    def put(self, key, auth):
        if request.form:
            data = request.form
        elif request.data:
            data = json.loads(request.data)
        else:
            raise request.form['This will raise a 400 and return immediately']
            # Unreachable
        value = data.get('value')
        if not value:
            return {
                'error': (
                    'Please PUT a new value. Eg. value=%s, not %s=%s. '
                    'If you want to create a new key-value pair, '
                    'POST to /key/' % (
                        data.values()[0],
                        data.keys()[0],
                        data.values()[0]
                    )
                )
            }, 400
        r.hset(auth, key, value)
        return {
            key: value
        }


class NewStore(Resource):
    @requires_auth
    def post(self, auth):
        if request.data:
            data = json.loads(request.data)
            key, value = data.popitem()
        elif request.form:
            key = request.form.keys()[0]
            value = request.form[key]
        else:
            raise request.form['This will raise a 400 and return immediately']
            # Unreachable
        r.hset(auth, key, value)
        return {
            key: value
        }

api.add_resource(NewStore, '/key/')
api.add_resource(Store, '/key/<string:key>')

ADMINS = ['tristram@oaten.name']
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(
        os.getenv('FLASK:EMAIL_HOST'),
        'server-error@stord.io',
        ADMINS,
        'stord.io error'
    )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('FLASK:PORT'))
    app.run(host='0.0.0.0', port=port)
