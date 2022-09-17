from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("prova.html")