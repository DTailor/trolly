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
    DIRECTION_TYPE = ((1, 'UPWARD'), (2, 'BACKWARD'))
    name = models.CharField(max_length=100, verbose_name=u'Station', blank=True, null=True)
    type = models.IntegerField(choices=DIRECTION_TYPE, verbose_name=u'Direction', blank=True, null=True)
    lat = models.CharField(max_length=15, verbose_name=u'Latitude')
    long = models.CharField(max_length=15, verbose_name=u'Longitude')

    def __unicode__(self):
        if(self.name):
            return "{0} - {1}".format(self.name, self.get_type_display())
        return "{0} - {1}".format(self.lat, self.long)

    def save(self, *args, **kwargs):
        self.lat = self.lat.replace(',','.')
        self.long = self.long.replace(',','.')
        super(GeoLocation, self).save(*args, **kwargs)

class StationStop(models.Model):
    """
    Model responsible for holding station stops for a certain route
    """
    WEEKDAY_CHOICES = ((1,'Mon-Fri'), (2, 'Sat'), (3, 'Sun'))
    station = models.ForeignKey(Station, verbose_name=u'Station')
    location = models.ForeignKey(GeoLocation, verbose_name=u'Geo Location', blank=True, null=True)
    order_nr = models.IntegerField(u'Order number')
    day_type = models.IntegerField(choices=WEEKDAY_CHOICES, verbose_name=u'Weekday Type')

    def __unicode__(self):
        return unicode(self.station)


class Route(models.Model):
    """
    Model responsible for trolleybus routes
    """
    nr = models.IntegerField(u'Route Number')
    stops = models.ManyToManyField(StationStop)

    def __unicode__(self):
        return unicode(self.nr)


class StopTime(models.Model):
    """
    Model responsible for holding trolleybus stop times
    """
    time = models.DateTimeField()
    station = models.ForeignKey(StationStop, related_name='stopstime', blank=True, null=True)
    route = models.ForeignKey(Route, related_name='route', blank=True, null=True)
    def __unicode__(self):
        return "{0} - {1}".format(self.time, self.station)


class WayPoint(models.Model):
    """
    Model responsible for holding the waypoints for a certain route
    """
    WAYPOINT_TYPE = ((1, 'UPWARD'), (2, 'BACKWARD'))
    lat = models.CharField(max_length=15, verbose_name=u'Latitude')
    long = models.CharField(max_length=15, verbose_name=u'Longitude')
    w_order = models.IntegerField(blank=True, null=True)
    route = models.ForeignKey(Route, related_name='waypoints')
    type = models.IntegerField(choices=WAYPOINT_TYPE, verbose_name=u'Direction',
                                blank=True, null=True)

    def __unicode__(self):
        return "{0} - {1}, {2}".format(self.route, self.lat, self.long)
