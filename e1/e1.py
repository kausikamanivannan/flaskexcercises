from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    return f"<h1>{now}</h1>"

if __name__ == "__main__":
    app.run()