# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WayPoint'
        db.create_table(u'faver_waypoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('long', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('w_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(related_name='waypoints', to=orm['faver.Route'])),
            ('type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'faver', ['WayPoint'])


    def backwards(self, orm):
        # Deleting model 'WayPoint'
        db.delete_table(u'faver_waypoint')


    models = {
        u'faver.geolocation': {
            'Meta': {'object_name': 'GeoLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'long': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'route': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'route'", 'null': 'True', 'to': u"orm['faver.Route']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'stopstime'", 'null': 'True', 'to': u"orm['faver.StationStop']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'faver.waypoint': {
            'Meta': {'object_name': 'WayPoint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'long': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'waypoints'", 'to': u"orm['faver.Route']"}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'w_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['faver']