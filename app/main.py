import sys
sys.path.append('.')

from flask import Flask, render_template, request, Response
from util.mapGenerator import MapGenerator
import requests
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home/map")
def goToMap():
    return render_template("map.html") 

@app.route('/styles/basic-preview/<path:url>')
def proxy_maptiles(url):
    maptiles_server_url = f'http://maptiles_server:80/styles/basic-preview/{url}'
    response = requests.get(maptiles_server_url)
    return Response(response.content, content_type='image/png')

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=2323)