from webserver.app import app

def main():
    app.run(host="0.0.0.0", debug=True, port=5000)

if __name__ == "__main__":
    main()
