from django.contrib import admin

from .models import Station, Route, StationStop, StopTime, GeoLocation

class StationAdmin(admin.ModelAdmin):
    pass

class GeoLocationAdmin(admin.ModelAdmin):
    pass

class RouteAdmin(admin.ModelAdmin):
    pass

class StationStopAdmin(admin.ModelAdmin):
    list_display = ('station', 'order_nr')

class StopTimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(StationStop, StationStopAdmin)
admin.site.register(StopTime, StopTimeAdmin)
admin.site.register(GeoLocation, GeoLocationAdmin)
