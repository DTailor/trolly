# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeoLocation'
        db.create_table(u'faver_geolocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('long', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'faver', ['GeoLocation'])

        # Deleting field 'Station.long'
        db.delete_column(u'faver_station', 'long')

        # Deleting field 'Station.lat'
        db.delete_column(u'faver_station', 'lat')

        # Adding field 'StationStop.location'
        db.add_column(u'faver_stationstop', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faver.GeoLocation'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'GeoLocation'
        db.delete_table(u'faver_geolocation')

        # Adding field 'Station.long'
        db.add_column(u'faver_station', 'long',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Station.lat'
        db.add_column(u'faver_station', 'lat',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'StationStop.location'
        db.delete_column(u'faver_stationstop', 'location_id')


    models = {
        u'faver.geolocation': {
            'Meta': {'object_name': 'GeoLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'long': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'faver.route': {
            'Meta': {'object_name': 'Route'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nr': ('django.db.models.fields.IntegerField', [], {}),
            'stops': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['faver.StationStop']", 'symmetrical': 'False'})
        },
        u'faver.station': {
            'Meta': {'object_name': 'Station'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rtec_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'faver.stationstop': {
            'Meta': {'object_name': 'StationStop'},
            'day_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faver.GeoLocation']", 'null': 'True', 'blank': 'True'}),
            'order_nr': ('django.db.models.fields.IntegerField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faver.Station']"})
        },
        u'faver.stoptime': {
            'Meta': {'object_name': 'StopTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'stopstime'", 'null': 'True', 'to': u"orm['faver.StationStop']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['faver']