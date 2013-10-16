# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Ad.image'
        db.alter_column('frontend_ad', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Ad.link'
        db.alter_column('frontend_ad', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))


    def backwards(self, orm):
        
        # Changing field 'Ad.image'
        db.alter_column('frontend_ad', 'image', self.gf('models.ImageField')())

        # Changing field 'Ad.link'
        db.alter_column('frontend_ad', 'link', self.gf('models.URLField')())


    models = {
        'frontend.ad': {
            'Meta': {'object_name': 'Ad'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['frontend']
