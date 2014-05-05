from django.contrib import admin

from .models import Station, Route, StationStop, StopTime

class StationAdmin(admin.ModelAdmin):
    pass

class RouteAdmin(admin.ModelAdmin):
    pass

class StationStopAdmin(admin.ModelAdmin):
    pass

class StopTimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Station, StationStopAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(StationStop, StationStopAdmin)
admin.site.register(StopTime, StopTimeAdmin)
