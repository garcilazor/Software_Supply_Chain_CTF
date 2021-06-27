import logging
import traceback
import time
import os

from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename

ROOT_SERVER_DIRECTORY = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(ROOT_SERVER_DIRECTORY, "uploads")
DATETIME_FORMAT = "%Y-%m-%d:%H:%M:%S"
MAXIMUM_FILE_AGE_SECONDS = 200

app = Flask(__name__)

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
    token = request.values.get('token')
    if token not in acceptable_tokens:
        return "Please supply a valid Trov-Token\n", 401
    elif 'file' not in request.files:
        return "You did not upload any file.\n", 401
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_directory = os.path.join(UPLOAD_FOLDER, token)
    file_location = os.path.join(file_directory, filename)
    os.makedirs(file_directory, exist_ok=True)
    prune_upload_directory()
    file.save(file_location)
    return "Upload successful.\n", 200

def prune_upload_directory():
    for client_upload_folder in os.listdir(UPLOAD_FOLDER):
        client_upload_folder_absolute = os.path.join(UPLOAD_FOLDER, client_upload_folder)
        for uploaded_file in os.listdir(client_upload_folder_absolute):
            uploaded_file_absolute = os.path.join(client_upload_folder_absolute, uploaded_file)
            upload_time = os.path.getmtime(uploaded_file_absolute)
            age = time.time() - upload_time
            if age > MAXIMUM_FILE_AGE_SECONDS:
                os.remove(uploaded_file_absolute)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def generic_error_handler(e):
    logger.error(f"The following exception occurred when responding to a request: {traceback.format_exc()}")
    return "The webapp encountered an un-handled exception. Please contact the author.\n", 500
