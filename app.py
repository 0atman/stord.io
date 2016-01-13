import os

from flask import Flask, request
from flask.ext import admin
from flask import render_template
from redis import Redis, StrictRedis
from flask_admin.contrib import rediscli
from flask_restful import Resource, Api

# Create application
app = Flask(__name__)
app.debug=True
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
r = StrictRedis(host='db', port=6379, db=0)

# Flask views
@app.route('/')
def index():
    return render_template('index.html')

api = Api(app)

class Store(Resource):
    def get(self, key):
        return r.get(key)

    def put(self, key):
        return r.set(key, request.form['data'])

api.add_resource(Store, '/store/<string:key>')


if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, 'Simple Models')
    admin.add_view(rediscli.RedisCli(Redis(host='db')))
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
