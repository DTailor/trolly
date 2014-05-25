var map;
var waypoints, route;
$(document).ready(function() {
    map = L.map('map').setView([47.03160, 28.82177], 13);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    map.locate({
        setView: true,
        maxZoom: 18
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
        marker.on('click', showMinutesLeft)
        markers.push(marker)
    }
    $('#remove-waypoints').on('click', function() {
        if (typeof waypoints != 'undefined') {
            map.removeLayer(waypoints);
        }
        $('#waypoints .ui-btn-active').removeClass('ui-btn-active')
        go_schedule_tab();
    });
    $('#go-back').on('click', function(){
        go_schedule_tab();
    })
    $('.route-btn').on('click', function() {
        btn = $(this);
        $('#waypoints .ui-btn-active').removeClass('ui-btn-active')
        btn.parent().addClass('ui-btn-active');
        draw_route(btn.val())
        go_schedule_tab();
    });
});
var current_marker;

function go_schedule_tab() {
    $('#schedule_button').removeClass('ui-btn-active')
    $('#return_map').click();
}

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

function showMinutesLeft() {
    current_marker = this;
    var station_id = this.station_id
    var request = $.ajax({
        url: variables['get_station_minutes_left'],
        type: "GET",
        data: {
            station_id: station_id
        },
        dataType: "html"
    });
    request.done(function(msg) {
        var data = $.parseJSON(msg);
        var template = $('#station-schedule').html();
        Mustache.parse(template); // optional, speeds up future uses
        var rendered = Mustache.render(template, data);
        current_marker.bindPopup(rendered).openPopup();
        $('.leaflet-popup').on("click", ".table-row", function() {
            route_name = $(this).attr('data-route')
            draw_route(route_name);
        });
    });
    request.fail(function(jqXHR, textStatus) {
        alert("Request failed: " + textStatus);
    });
}

function draw_route(route_name) {
    var request = $.ajax({
        url: variables['route_waypoints'],
        type: "GET",
        data: {
            route_name: route_name
        },
        dataType: "html"
    });
    request.done(function(msg) {
        var data = $.parseJSON(msg);
        coords = data.coords
        if (typeof waypoints != 'undefined') {
            map.removeLayer(waypoints);
        }
        route = [{
            type: "LineString",
            "coordinates": coords.forward.concat(coords.backward)
        }, ];
        waypoints = L.geoJson(route);
        waypoints.addTo(map);
    });
    request.fail(function(jqXHR, textStatus) {
        alert("Request failed: " + textStatus);
    });
}
$(document).delegate('.ui-navbar a', 'click', function() {
    $(this).addClass('ui-btn-active');
    $('.content_div').hide();
    $('#' + $(this).attr('data-href')).show();
});
