from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import GeoLocation, StopTime, StationStop
from django.core import serializers
import json
from .utils import get_normalized_time


def index(request):
    stations = serializers.serialize(
        'json', GeoLocation.objects.all(), fields=('lat', 'long', 'name'))
    return render_to_response('pages/index.html', {'locations': stations})


def show_schedule(request):
    schedule = dict()
    st_lat = request.GET.get('latitude', '46.9773091')
    st_lon = request.GET.get('longitude', '28.8706002')
    geo_point = GeoLocation.objects.get(lat=st_lat, long=st_lon)
    station_stops = StationStop.objects.filter(location=geo_point)

    now = get_normalized_time()
    stop_times = StopTime.objects.filter(
        station__in=station_stops, time__gte=now)
    for stop_time in stop_times:
        pass
    return schedule


def get_station_schedule(request):
    if request.method == 'GET':
        geo_id = request.GET.get('station_id', False)
        if geo_id:
            geo_point = GeoLocation.objects.get(id=int(geo_id))
            station_stops = StationStop.objects.filter(location=geo_point)
            now = get_normalized_time()
            stop_times = StopTime.objects.filter(
                station__in=station_stops, time__gte=now).order_by('time')[:10]
            stop_times_data = []
            for stop_time in stop_times:
                tmp_dict = {stop_time.route.nr: "{0:02d}:{1:02d}".format(
                    stop_time.time.hour, stop_time.time.minute)}
                stop_times_data.append(tmp_dict)
            data = {'schedule': stop_times_data, 'station': geo_point.name}
            data = json.dumps(data)
            return HttpResponse(data)
    return HttpResponse(status=404)


def get_station_minutes_left(request):
    if request.method == 'GET':
        geo_id = request.GET.get('station_id', False)
        if geo_id:
            geo_point = GeoLocation.objects.get(id=int(geo_id))
            station_stops = StationStop.objects.filter(location=geo_point)
            now = get_normalized_time()
            stop_times = StopTime.objects.filter(
                station__in=station_stops, time__gte=now).order_by('time')[:10]
            stop_times_data = []
            for stop_time in stop_times:
                minutes_left = (stop_time.time - now).seconds / 60
                tmp_dict = {stop_time.route.nr: "{0}".format(minutes_left)}
                stop_times_data.append(tmp_dict)
            data = {'schedule': stop_times_data, 'station': geo_point.name}
            data = json.dumps(data)
            return HttpResponse(data)
    return HttpResponse(status=404)
