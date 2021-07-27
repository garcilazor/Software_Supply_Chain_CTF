from flask import redirect, request, url_for, session
from flask.views import MethodView
import flagModel
import mapModel

class Plant(MethodView):

    # redirect to home page
    def get(self):
        return redirect(url_for('index'))

    # submit form data from html page
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """

        # get database of flags
        model = flagModel.get_model()

        # get NASA API client
        client = mapModel.get_client()

        # get session position data
        height = 0
        row = 0
        column = 0 
        if 'hgt' in session:
            height = session['hgt']
            row = session['row']
            column = session['col']

        # get flag/tile co-ord bounds
        flagBounds = client.getFlagBounds(height, row, column)
        tileBounds = client.getBounds(height)

        # calculate overall co-ords of new flag
        x = int(request.form['x'])*((flagBounds['xr'] - flagBounds['xl']) // 20) + flagBounds['xl']
        y = int(request.form['y'])*((flagBounds['yr'] - flagBounds['yl']) // 10) + flagBounds['yl']

        # post new flag in flag database
        model.insert(x, y, request.form['message'])

        return redirect(url_for('index'))

