from django.contrib import admin

from .models import Station, Route, StationStop, StopTime, \
                    GeoLocation, WayPoint

class StationAdmin(admin.ModelAdmin):
    pass

class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)

class RouteAdmin(admin.ModelAdmin):
    pass

class StationStopAdmin(admin.ModelAdmin):
    list_display = ('station', 'location', 'order_nr')

class StopTimeAdmin(admin.ModelAdmin):
    pass

class WayPointAdmin(admin.ModelAdmin):
    list_display = ('route', 'lat', 'long')


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(StationStop, StationStopAdmin)
admin.site.register(StopTime, StopTimeAdmin)
admin.site.register(GeoLocation, GeoLocationAdmin)
admin.site.register(WayPoint, WayPointAdmin)
