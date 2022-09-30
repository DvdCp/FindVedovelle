var locate_control_52631e7305a8ed78b7fafd5a43e30548 = L.control.locate(
    {"enableHighAccuracy": true, "onLocationError": askForGPS}
).addTo(map_053b87bcca479b6e80be96a907821a31);

    locate_control_52631e7305a8ed78b7fafd5a43e30548.start();

function askForGPS(){
    if(navigator.geolocation)
    {
        alert('Please enable GPS localization on your phone Settings and reload the page');
    }   
    else
    {
        alert("Enable to get geolocalization for this browser.... Sorry :( ");
    }
}