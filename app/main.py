import sys
sys.path.append('.')

from flask import Flask, render_template
from util.mapGenerator import MapGenerator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home/map")
def goToMap():
    return render_template("map.html") 

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=2323)