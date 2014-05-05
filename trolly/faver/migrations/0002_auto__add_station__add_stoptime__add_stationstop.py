# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table(u'faver_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('long', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rtec_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'faver', ['Station'])

        # Adding model 'StopTime'
        db.create_table(u'faver_stoptime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stopstime', to=orm['faver.StationStop'])),
        ))
        db.send_create_signal(u'faver', ['StopTime'])

        # Adding model 'StationStop'
        db.create_table(u'faver_stationstop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faver.Station'])),
            ('order_nr', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'faver', ['StationStop'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table(u'faver_station')

        # Deleting model 'StopTime'
        db.delete_table(u'faver_stoptime')

        # Deleting model 'StationStop'
        db.delete_table(u'faver_stationstop')


    models = {
        u'faver.station': {
            'Meta': {'object_name': 'Station'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'long': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rtec_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'faver.stationstop': {
            'Meta': {'object_name': 'StationStop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_nr': ('django.db.models.fields.IntegerField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faver.Station']"})
        },
        u'faver.stoptime': {
            'Meta': {'object_name': 'StopTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stopstime'", 'to': u"orm['faver.StationStop']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['faver']