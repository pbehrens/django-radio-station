# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'DJ.slug'
        db.alter_column('station_dj', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50))

        # Changing field 'DJ.user'
        db.alter_column('station_dj', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Changing field 'Spot.dj'
        db.alter_column('station_spot', 'dj_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['station.DJ']))

        # Changing field 'Spot.schedule'
        db.alter_column('station_spot', 'schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['station.Schedule']))

        # Changing field 'Spot.show'
        db.alter_column('station_spot', 'show_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['station.Show']))

        # Changing field 'Show.image'
        db.alter_column('station_show', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Show.slug'
        db.alter_column('station_show', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50))


    def backwards(self, orm):
        
        # Changing field 'DJ.slug'
        db.alter_column('station_dj', 'slug', self.gf('models.SlugField')(unique=True))

        # Changing field 'DJ.user'
        db.alter_column('station_dj', 'user_id', self.gf('models.OneToOneField')(orm['auth.User']))

        # Changing field 'Spot.dj'
        db.alter_column('station_spot', 'dj_id', self.gf('models.ForeignKey')(orm['station.DJ']))

        # Changing field 'Spot.schedule'
        db.alter_column('station_spot', 'schedule_id', self.gf('models.ForeignKey')(orm['station.Schedule']))

        # Changing field 'Spot.show'
        db.alter_column('station_spot', 'show_id', self.gf('models.ForeignKey')(orm['station.Show']))

        # Changing field 'Show.image'
        db.alter_column('station_show', 'image', self.gf('models.ImageField')())

        # Changing field 'Show.slug'
        db.alter_column('station_show', 'slug', self.gf('models.SlugField')(unique=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 16, 9, 54, 59, 294960)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 16, 9, 54, 59, 294544)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'station.dj': {
            'Meta': {'object_name': 'DJ'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'station.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'station.show': {
            'Meta': {'object_name': 'Show'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'schedule': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['station.Schedule']", 'through': "orm['station.Spot']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'special_program': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'station.spot': {
            'Meta': {'object_name': 'Spot'},
            'day_of_week': ('django.db.models.fields.IntegerField', [], {}),
            'dj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['station.DJ']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offset': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'repeat_every': ('django.db.models.fields.IntegerField', [], {}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['station.Schedule']"}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['station.Show']"})
        }
    }

    complete_apps = ['station']
