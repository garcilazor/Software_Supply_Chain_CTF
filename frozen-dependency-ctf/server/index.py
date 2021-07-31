from flask import render_template, session, request, url_for, redirect
from flask.views import MethodView
from owslib.wmts import WebMapTileService
import mapModel
import flagModel

# load html page, loaded with map and flag data
class Index(MethodView):
    def get(self):

        # get database of flags
        model = flagModel.get_model()

        # initialize NASA API client
        client = mapModel.get_client()

        # get user's heigh, row, and column from cookie data,
        # if it exists. otherwise, default to 0 for all
        height = 0
        row = 0
        column = 0
        if 'hgt' in session:
            height = session['hgt']
            row = session['row']
            column = session['col']

        # get map tiles
        tiles = client.getTiles(height, row, column)

        # get flag/tile co-ord bounds
        flagBounds = client.getFlagBounds(height, row, column)
        tileBounds = client.getBounds(height)

        # do math necessary to find flag boundaries of current frame
        # xchunk = flagBounds[0]//(tileBounds[0]+2)
        # ychunk = flagBounds[1]//(tileBounds[1]+1)
        # xlbound = column * xchunk
        # xrbound = (column+2) * xchunk
        # ylbound = row * ychunk
        # yrbound = (row+1) * ychunk

        # get all flags within current frame
        flags = [dict(x=row[0],
                y=row[1],
                message=row[2])
                for row in model.select()]

        # filter out all flags not in current frame
        flags2 = [i for i in flags if ((i['y'] > flagBounds['yl']) and 
                                        (i['y'] < flagBounds['yr'])) and
                                        ((i['x'] > flagBounds['xl']) and 
                                        (i['x'] < flagBounds['xr']))]

        # calculate html image co-ords within frame, 
        # modify flags appropriately
        for i, flag in enumerate(flags2):
            flags2[i]['x'] = int(((flag['x'] - flagBounds['xl']) / (flagBounds['xr'] - flagBounds['xl'])) *20 *23.3)
            flags2[i]['y'] = int(((flag['y'] - flagBounds['yl']) / (flagBounds['yr'] - flagBounds['yl'])) *10 *24.4)

        # get map bounds
        bounds = client.getBounds(tiles[0])

        # load page
        return render_template('index.html', coords=[tiles[0], tiles[1], tiles[2]], tiles=tiles[3], flags=flags2, bounds=bounds) 


