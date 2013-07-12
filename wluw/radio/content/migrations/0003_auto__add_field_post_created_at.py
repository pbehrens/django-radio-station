# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.created_at'
        db.add_column('content_post', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2013, 7, 11), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Post.created_at'
        db.delete_column('content_post', 'created_at')


    models = {
        'content.post': {
            'Meta': {'object_name': 'Post'},
            'coverImage': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {'max_length': '200000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['content']
