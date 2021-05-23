from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/uploader")
def uploader_download():
    return send_file("static/uploader")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)