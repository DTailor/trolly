from django.shortcuts import render_to_response
from .models import GeoLocation
from django.core import serializers


def index(request):
    stations = serializers.serialize('json', GeoLocation.objects.all(), fields=('lat', 'long', 'name'))
    return render_to_response('pages/index.html', {'locations': stations})