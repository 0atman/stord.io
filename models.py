import datetime

from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


class User(db.Document):
    name = db.StringField(max_length=40)
    password = db.StringField(max_length=40)

    def __unicode__(self):
        return self.name


class Record(db.Document):
    key = db.StringField(max_length=20)
    value = db.StringField(max_length=20)
