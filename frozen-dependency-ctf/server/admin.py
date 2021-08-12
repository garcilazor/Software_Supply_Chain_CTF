from flask import render_template, request, url_for, session
from flask.views import MethodView
from utils import SimpleDB
from flask_security import current_user

class Admin(MethodView):

    # load and display user data
    def get(self):

        #get db
        db, user_datastore, security = SimpleDB.get()
        
        #best guess for getting user -- try user_datastore.find_user() if it does not work
        #curr_user = user_datastore.find_user(email
        username = current_user.calc_username()
        profile, secret = current_user.get_data()

        return render_template('admin.html', username=username, profile=profile, secret=secret)

