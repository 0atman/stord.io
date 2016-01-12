import os

from flask import Flask
from flask.ext import admin
from flask import render_template
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

from models import *
from admin import UserView

# Create application
app = Flask(__name__)
app.debug=True
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {
    'DB': 'testing'
}

# Create models
connect(
    'flask-basic',
    host=os.environ.get(
        'MONGOLAB_URI',
        'mongodb://db/restr'
    )
)
db = MongoEngine()
db.init_app(app)


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, 'Simple Models')

    # Add views
    admin.add_view(UserView(User))
    admin.add_view(ModelView(Record))

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
