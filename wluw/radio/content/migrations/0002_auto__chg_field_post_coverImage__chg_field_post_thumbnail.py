# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Post.coverImage'
        db.alter_column('content_post', 'coverImage', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'Post.thumbnail'
        db.alter_column('content_post', 'thumbnail', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Post.coverImage'
        db.alter_column('content_post', 'coverImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Post.thumbnail'
        db.alter_column('content_post', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    models = {
        'content.post': {
            'Meta': {'object_name': 'Post'},
            'coverImage': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {'max_length': '200000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['content']
