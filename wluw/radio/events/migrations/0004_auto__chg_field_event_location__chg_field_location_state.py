# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Event.location'
        db.alter_column('events_event', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Location'], null=True))

        # Changing field 'Location.state'
        db.alter_column('events_location', 'state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2, null=True))


    def backwards(self, orm):
        
        # Changing field 'Event.location'
        db.alter_column('events_event', 'location_id', self.gf('models.ForeignKey')(orm['events.Location'], null=True))

        # Changing field 'Location.state'
        db.alter_column('events_location', 'state', self.gf('USStateField')(null=True))


    models = {
        'events.event': {
            'Meta': {'ordering': "['-date', '-time_start']", 'object_name': 'Event'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Location']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'time_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_start': ('django.db.models.fields.TimeField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'events.location': {
            'Meta': {'ordering': "['name']", 'object_name': 'Location'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']
