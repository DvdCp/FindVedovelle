from flask import Flask, render_template
import subprocess, shlex
import docker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home/map")
def goToMap():
    return render_template("map.html") 

if __name__ == "__main__":

    # Check if MapTiler/Server Docker image is running
    CONTAINER_NAME = "maptiles_server"
    IMAGE_NAME = "maptiler/tileserver-gl"

    docker_client = docker.from_env()

    try :
        container = docker_client.containers.get(CONTAINER_NAME)

    except docker.errors.NotFound as ex:
        #TODO check here what is the cwd 
        args = shlex.split(r"docker run --name maptiles_server --rm -it -v C:\\Users\\David\\Git\\BeviVedovelle\\app\\static\\assets\\maptiles:/data -p 3065:80 maptiler/tileserver-gl --mbtiles 2017-07-03_italy_milan.mbtiles")
        docker_container = subprocess.Popen(args)

    # app.run(debug=True, host='0.0.0.0')