from flask import render_template
from flask.views import MethodView

class Donate(MethodView):

    def get(self):
        return render_template('donate.html')

