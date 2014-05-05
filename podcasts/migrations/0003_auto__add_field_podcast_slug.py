# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Podcast.slug'
        db.add_column(u'podcasts_podcast', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=None, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Podcast.slug'
        db.delete_column(u'podcasts_podcast', 'slug')


    models = {
        u'podcasts.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['podcasts.PodcastCategory']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'explicit': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_href': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '2000'}),
            'owner_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'podcasts.podcastcategory': {
            'Meta': {'object_name': 'PodcastCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['podcasts.PodcastCategory']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'podcasts.podcastenclosure': {
            'Meta': {'object_name': 'PodcastEnclosure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'max_length': '16'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'audio/mpeg'", 'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2000'})
        },
        u'podcasts.podcastepisode': {
            'Meta': {'object_name': 'PodcastEpisode'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enclosure': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['podcasts.PodcastEnclosure']", 'unique': 'True'}),
            'explicit': ('django.db.models.fields.BooleanField', [], {}),
            'guid': ('django.db.models.fields.CharField', [], {'default': "'pe:9d5784ad-bf52-4190-a7af-214ef2c3faac'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_href': ('django.db.models.fields.URLField', [], {'max_length': '2000'}),
            'podcast': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['podcasts.Podcast']"}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['podcasts']