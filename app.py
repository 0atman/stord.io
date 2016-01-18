import os
from functools import wraps
import json

from flask import Response, redirect
from flask import Flask, request
from flask import render_template
from redis import StrictRedis
from flask_restful import Resource, Api, reqparse

# Create application
app = Flask(__name__)
app.debug = False

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = 'a908df79a8df7ga89dfg123456790'
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


@app.route('/')
def index():
    return redirect("http://www.stord.io", 301)

api = Api(app)


class Store(Resource):
    @requires_auth
    def get(self, key, auth):
        value = r.hget(auth, key)
        if value is None:
            return {
                'Not found': key
            }, 404
        else:
            return {
                'success': value
            }

    @requires_auth
    def post(self, key, auth):
        if request.form:
            data = request.form['data']
        elif request.data:
            data = json.loads(request.data)['data']
        else:
            raise request.form['This will raise a 400 and return immediately']
            # Unreachable
        if r.hset(auth, key, data) == 0:
            return {
                'success': data
            }
        else:
            return 'ERROR', 500

    put = post

api.add_resource(Store, '/key/<string:key>')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
