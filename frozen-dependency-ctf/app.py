"""
Mars rover App
"""

import flask
import os
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_security.models import fsqla
from utils import db_setup
from index import Index
from move import Move
from plant import Plant
from admin import Admin

app = flask.Flask(__name__)

# generate secret key for session cookies
app.secret_key = b'U\xe7\xb7\x9c\x01\x82\xfbf\xd8\xaf\xde i\xdb\xac\xe4'

# user account database setup
db, security = db_setup(app)

# home page (where all the magic happens)
app.add_url_rule('/',
		view_func=Index.as_view('index'),
		methods=['GET'])

# form submission processing page, used to change position on map
app.add_url_rule('/move/',
                view_func=Move.as_view('move'),
                methods=['GET', 'POST'])

# form submission processing page, used to add a flag to the map
app.add_url_rule('/plant/',
                view_func=Plant.as_view('plant'),
                methods=['GET', 'POST'])

# admin page
admin_view = login_required(Admin.as_view('admin'))
app.add_url_rule('/admin/',
                view_func=admin_view,
                methods=['GET'])

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=8000, debug=True)


