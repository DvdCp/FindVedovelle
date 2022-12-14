from folium import Map, Marker
from folium.plugins import LocateControl
import json

MILAN_COORDINATE = [45.465225, 9.186344]

class MapGenerator:

    def createVedovellaButton(lat: float, long: float) -> str:
        """
            Create a button for a Vedovella located with lat and long coords
        """

        button = """<a href="https://www.google.com/maps/search/?api=1&query={0}%2C{1}" target="_blank">
                        <button>Go !</button>
                    </a>""".format(lat, long)

        return button

    def createMap(location: list, zoom_start=14):
        
        # First create the map
        map = Map(  location=location, 
                    zoom_start=zoom_start, 
                    # tiles='https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png',  
                    tiles='http://localhost:3065/styles/basic-preview/{z}/{x}/{y}.png',  
                    attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
                )

        # Loading vedovelle JSON file
        f = open(r"resources\Vedovelle_final.json", "r")
        vedovelle_list = json.load(f)

        for vedovella in vedovelle_list:

            # Getting this vedovella info (LAT & LONG)
            vedovella_pos = [vedovella["LAT_Y_4326"], vedovella["LONG_X_4326"]]
            vedovella_popup = MapGenerator.createVedovellaButton(vedovella["LAT_Y_4326"], vedovella["LONG_X_4326"])

            Marker(vedovella_pos, popup=vedovella_popup).add_to(map)

        # Locate user real-time position
        LocateControl(auto_start=True, enableHighAccuracy=True).add_to(map)

        # Save map in resources folder
        map.save(r"templates\map.html")

if __name__ == "__main__":
    MapGenerator.createMap(MILAN_COORDINATE)
