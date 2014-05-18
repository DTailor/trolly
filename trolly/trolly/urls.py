from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'faver.views.index', name='home'),

                       url(r'^get_station_schedule/$',
                           'faver.views.get_station_schedule',
                           name='get_station_schedule'),

                       url(r'^get_station_minutes_left/$',
                           'faver.views.get_station_minutes_left',
                           name='get_station_minutes_left'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
