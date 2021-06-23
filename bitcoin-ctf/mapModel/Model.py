from owslib.wmts import WebMapTileService

# constant variables, to be changed should I ever wish to expand this web to 
# print more than two tiles per screen. These numbers are hardcoded in other
# files of this app, so don't change them here. Errors will occur!
X_TILES_PER_FRAME = 2
Y_TILES_PER_FRAME = 1

# Class to store the position and image url for the current tile.
# Currently only the url is used, but the position data would be necessary 
# if the rest of the app was changed to print more than two tiles per screen.
class tile():
    def __init__(self, img, row, column):
        self.url = img.geturl()
        self.row = row
        self.column = column

# a class for interacting with the WMTS client, which itself interacts with
# NASA's Mars Trek API
class model():

    # initialize WMTS client, and connect it to the Mars Trek API
    def __init__(self):
        self.wmtsClient = WebMapTileService("https://api.nasa.gov/mars-wmts/catalog/Mars_Viking_MDIM21_ClrMosaic_global_232m/1.0.0/WMTSCapabilities.xml")

    # get tiles necessary for requested frame
    def getTiles(self, height, row, column):
        """
        Gets tiles for current frame
        :param height: Int
        :param row: Int
        :param column: Int
        :return: List
        """

        # check height bound
        maxHeight = len(self.wmtsClient.tilematrixsets["default028mm"].tilematrix)-1
        if height > maxHeight:
            height = maxHeight

        # get info on tile matrix
        tileMatrix = self.wmtsClient.tilematrixsets["default028mm"].tilematrix[str(height)]

        # check row and column limits
        if(tileMatrix.matrixwidth-X_TILES_PER_FRAME < column):
            column = tileMatrix.matrixwidth-X_TILES_PER_FRAME
        if(tileMatrix.matrixheight-Y_TILES_PER_FRAME < row):
            row = tileMatrix.matrixheight-Y_TILES_PER_FRAME

        # set up list to store tiles
        # tiles will be a tuple containing tile url, column position, and row
        # position
        tiles = []

        # pull NASA Mars Trek images
        for y in range(Y_TILES_PER_FRAME):
            for x in range(X_TILES_PER_FRAME):

                # pull present image tile from NASA Mars Trek
                image = self.wmtsClient.gettile(layer="Mars_Viking_MDIM21_ClrMosaic_global_232m", 
                        tilematrix=str(height), 
                        row=(row+y), 
                        column=(column+x))

                #create tile, and append it to tiles
                tiles.append(tile(image, row+y, column+x))

        # set up return data, consisting of position data and tiles
        output = [height, row, column, tiles]

        return output

    # retrieves max x/y co-ords at current zoom level
    def getBounds(self, height):
        """
        Retrieve c/y co-ord bounds at given height.
        :param height: Int
        :return: List
        """
        
        # check height bound
        maxHeight = len(self.wmtsClient.tilematrixsets["default028mm"].tilematrix)-1
        if height > maxHeight:
            height = maxHeight

        # get info on tile matrix
        tileMatrix = self.wmtsClient.tilematrixsets["default028mm"].tilematrix[str(height)]

        bounds = []

        # pull bounds from API
        bounds.append(tileMatrix.matrixwidth-X_TILES_PER_FRAME)
        bounds.append(tileMatrix.matrixheight-Y_TILES_PER_FRAME)

        return bounds

    # returns bounds for current frame that flags can posted within
    def getFlagBounds(self, height, row, column):
        """
        Gets flag bounds for current frame
        :param height: Int
        :param row: Int
        :param column: Int
        :return: Dict
        """

        # first, get matrix tile set
        tileMatrices = self.wmtsClient.tilematrixsets["default028mm"].tilematrix
        # get highest zoom tile set
        tileMatrix = tileMatrices[str(len(tileMatrices)-1)]

        # get tile bounds
        tileBounds = self.getBounds(height)

        # do math necessary to find flag boundaries of current frame
        xchunk = tileMatrix.matrixwidth//(tileBounds[0]+X_TILES_PER_FRAME)
        ychunk = tileMatrix.matrixheight//(tileBounds[1]+Y_TILES_PER_FRAME)
        xlbound = column * xchunk
        xrbound = (column+X_TILES_PER_FRAME) * xchunk
        ylbound = row * ychunk
        yrbound = (row+Y_TILES_PER_FRAME) * ychunk

        #return bounds
        return dict(xl=xlbound,
                xr=xrbound,
                yl=ylbound,
                yr=yrbound)




