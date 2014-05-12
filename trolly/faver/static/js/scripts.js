$(document).ready(function() {
    // create a map in the "map" div, set the view to a given place and zoom
    var map = L.map('map').setView([47.03160, 28.82177], 13);
    // add an OpenStreetMap tile layer
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    // add a marker in the given location, attach some popup content to it and open the popup

    var jsonStations = $.parseJSON(variables.locations);
    var station;
    for (var i = 0; i < jsonStations.length; i++) {
        station = jsonStations[i];
        console.log(station)
        L.marker([parseFloat(station.fields.lat), parseFloat(station.fields.long)]).addTo(map)
        .bindPopup(station.fields.name + ' - '+station.fields.lat + ' - ' +station.fields.long)
        .openPopup(); 
    }
    // L.marker([47.03160, 28.82177]).addTo(map);
});
