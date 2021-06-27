import logging
import traceback
import datetime
import os

from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/home/appuser/uploads"
DATETIME_FORMAT = "%Y-%m-%d:%H:%M:%S"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(format='%(asctime)s %(message)s', filename="webserver.log", filemode='a', level=logging.INFO)
logger = logging.getLogger(__name__)


# We really need to set up a DB one of these days.
acceptable_tokens = {
    "adf81eac-1cb4-4bc5-b35b-b50f986a989e",
    "7833cc2b-90fc-4384-bd50-3c1ed5bae942",
    "fae03684-07b3-42a8-b9dc-9fef10aa1f44",
    "735a566b-f572-4cac-ac6f-dc3f03c512ca",
    "ce3e2000-1730-4586-abf1-6574153831fb",
    "b54337b2-35ee-4bad-a74e-83f05394f393",
    "15694070-55e0-4c26-a0e3-f4b3b58a61c4",
    "88716a29-abce-40ea-9159-92e675c405d5",
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bash")
def uploader_download():
    return send_file("static/uploader")

@app.route("/upload/v1", methods=["POST"])
def handle_upload():
    token = request.args.get('token')
    if token not in acceptable_tokens:
        return "Please supply a valid Trov-Token\n", 401
    elif 'file' not in request.files:
        return "You did not upload any file.\n", 401
    file = request.files['file']
    prune_upload_directory()
    dt_string = datetime.datetime.now().strftime(DATETIME_FORMAT)
    file_location= f"{UPLOAD_FOLDER}/{token}/{dt_string}"
    filename = secure_filename(file.filename)
    file.save(file_location, filename)
    return "Upload successful.\n", 200

def prune_upload_directory():
    # TODO Remove old stuff
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def generic_error_handler(e):
    logger.error(f"The following exception occurred when responding to a request: {traceback.format_exc()}")
    return "The webapp encountered an un-handled exception. Please contact the author.\n", 500