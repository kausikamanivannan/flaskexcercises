from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

valid_organizations = ["org1", "org2", "org3", "org4", "org5"]
registrations = {}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    organization = request.form.get("organization")

    if not name or not organization:
        return redirect(url_for("index"))

    if organization not in valid_organizations:
        return redirect(url_for("index"))

    registrations[name] = organization

    return redirect(url_for("registrations"))

@app.route("/registrations", methods=["GET"])
def registrations():
    return render_template("registrations.html", registrations=registrations)

if __name__ == "__main__":
    app.run()
