from django.db import models


class Station(models.Model):
    """
    Model responsible for stations
    """
    name = models.CharField(max_length=255, verbose_name=u'Name')
    rtec_id = models.IntegerField(u'RTEC ID', blank=True, null=True)

    def __unicode__(self):
        return self.name


class GeoLocation(models.Model):
    """
    Model representing the geolocation
    of a certain station
    """
    lat = models.CharField(max_length=10, verbose_name=u'Latitude', blank=True, null=True)
    long = models.CharField(max_length=10, verbose_name=u'Longitude', blank=True, null=True)

    def __unicode__(self):
        return unicode("{0} - {1}".format(self.lat, self.long))


class StationStop(models.Model):
    """
    Model responsible for holding station stops for a certain route
    """
    WEEKDAY_CHOICES = ((1,'Mon-Fri'), (2, 'Sat'), (3, 'Sun'))
    station = models.ForeignKey(Station, verbose_name=u'Station')
    location = models.ForeignKey(GeoLocation, verbose_name=u'Geo Location')
    order_nr = models.IntegerField(u'Order number')
    day_type = models.IntegerField(choices=WEEKDAY_CHOICES, verbose_name=u'Weekday Type')

    def __unicode__(self):
        return unicode(self.station)


class StopTime(models.Model):
    """
    Model responsible for holding trolleybus stop times
    """
    time = models.DateTimeField()
    station = models.ForeignKey(StationStop, related_name='stopstime', blank=True, null=True)

    def __unicode__(self):
        return "{0} - {1}".format(self.time, self.station)


class Route(models.Model):
    """
    Model responsible for trolleybus routes
    """
    nr = models.IntegerField(u'Route Number')
    stops = models.ManyToManyField(StationStop)

    def __unicode__(self):
        return unicode(self.nr)
        