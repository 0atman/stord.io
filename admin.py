from flask.ext.admin.contrib.mongoengine import ModelView


class UserView(ModelView):
    column_filters = ['name']

    column_searchable_list = ('name', 'password')
