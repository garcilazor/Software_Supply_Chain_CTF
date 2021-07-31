from flask import session, request, url_for, redirect
from flask.views import MethodView
from owslib.wmts import WebMapTileService
import mapModel

class Move(MethodView):
    
    # redirect to home page
    def get(self):
        return redirect(url_for('index'))

    # use form data from html page to modify session cookie
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """

        session['hgt'] = int(request.form['height'])
        session['col'] = int(request.form['column'])
        session['row'] = int(request.form['row'])

        return redirect(url_for('index'))

