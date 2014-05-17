$(document).ready(function() {

    var map = L.map('map').setView([47.03160, 28.82177], 13);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    map.locate({
        setView: true,
        maxZoom: 16
    });


    function onLocationFound(e) {
        var radius = e.accuracy / 2;
        L.marker(e.latlng).addTo(map)
    }



    map.on('locationfound', onLocationFound);

    var jsonStations = $.parseJSON(variables.locations);
    var station;
    var markers = [];
    for (var i = 0; i < jsonStations.length; i++) {
        station = jsonStations[i]
        marker = L.marker([parseFloat(station.fields.lat), parseFloat(station.fields.long)])
            .addTo(map)
        marker.station_id = station.pk
        marker.id = i;
        marker.on('click', showSchedule)
        markers.push(marker)
    }

});


var current_marker;

function showSchedule() {
    current_marker = this;

    var station_id = this.station_id
    var request = $.ajax({
        url: variables['get_station_schedule'],
        type: "GET",
        data: {
            station_id: station_id
        },
        dataType: "html"
    });

    request.done(function(msg) {
        var data = $.parseJSON(msg);
        var popup = '';
        popup += data.station + "<br />"
        var schedule = data.schedule
        for (var i = 0; i < schedule.length; i++) {
            tmp_schedule = schedule[i]
            for (var route in tmp_schedule) {
                tmp_msg = route + " - " + tmp_schedule[route] + "<br />";
            }
            popup += tmp_msg;
        }
        current_marker.bindPopup(popup).openPopup();

    });

    request.fail(function(jqXHR, textStatus) {
        alert("Request failed: " + textStatus);
    });
}
