from flask import Flask, request, render_template, send_file
app = Flask(__name__)

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

@app.route("/uploader")
def uploader_download():
    return send_file("static/uploader")

@app.route("/upload", methods=["POST"])
def handle_upload():
    token = request.args.get('token')
    if token in acceptable_tokens:
        return 200
    return "Please supply a valid Trov-Token ", 401
