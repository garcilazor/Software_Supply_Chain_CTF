from flask import render_template, request, url_for, session
from flask.views import MethodView
import flagModel
import mapModel

class Admin(MethodView):

    # redirect to home page
    def get(self):
        return render_template('admin.html')

