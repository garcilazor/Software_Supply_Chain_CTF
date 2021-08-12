"""
Mars rover App
"""

import flask
import os
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_security.models import fsqla
import utils
from index import Index
from move import Move
from plant import Plant
from admin import Admin

app = flask.Flask(__name__)
app.config["SECURITY_CSRF_COOKIE_NAME"] = "XSRF-TOKEN"
app.config["WTF_CSRF_CHECK_DEFAULT"] = False
app.config["WTF_CSRF_TIME_LIMIT"] = None
app.config["SECURITY_CSRF_HEADER"] = "X-XSRF-TOKEN"
app.config["SECURITY_CSRF_COOKIE_REFRESH_EACH_REQUEST"] = False
app.config["SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS"] = True

# generate secret key for session cookies
app.secret_key = b'U\xe7\xb7\x9c\x01\x82\xfbf\xd8\xaf\xde i\xdb\xac\xe4'

# user account database setup
db, user_datastore, security = utils.db_setup(app)

@app.before_first_request
def create_users():
        db.create_all()
        user_datastore.create_role(
                name="admin",
                permissions={"admin-read", "admin-write", "user-read", "user-write"},
        )
        user_datastore.create_role(name="monitor", permissions={"admin-read", "user-read"})
        user_datastore.create_role(name="user", permissions={"user-read", "user-write"})
        user_datastore.create_role(name="reader", permissions={"user-read"})

        user_datastore.create_user(
                email="ramon@me.com", password="password", roles=["admin"], profile="I am a software developer who likes tuna. A lot.", secret="dh54HGF43gTY2y"
        )
        user_datastore.create_user(
                email="bill@me.com", password="password", roles=["monitor"]
        )
        real_user = user_datastore.create_user(
                email="jacob@me.com", password="password", roles=["user"]
        )
        user_datastore.create_user(
                email="reader@me.com", password="password", roles=["reader"]
        )

        db.session.commit()

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
admin_view = auth_required("session", "token")(Admin.as_view('admin'))
app.add_url_rule('/admin/',
                view_func=admin_view,
                methods=['GET'])

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=80, debug=True)


