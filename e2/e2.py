from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET"])
def result():
    try:
        number = int(request.args.get("number"))
    except (TypeError, ValueError):
        return render_template("result.html", error="Invalid input")
    
    if number % 2 == 0:
        message = "even"
    else:
        message = "odd"
    
    return render_template("result.html", number=number, message=message)

if __name__ == "__main__":
    app.run()
