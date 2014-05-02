# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Podcast'
        db.create_table(u'podcasts_podcast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=2000)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('copyright', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pubdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('owner_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image_href', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('explicit', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'podcasts', ['Podcast'])

        # Adding M2M table for field categories on 'Podcast'
        m2m_table_name = db.shorten_name(u'podcasts_podcast_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('podcast', models.ForeignKey(orm[u'podcasts.podcast'], null=False)),
            ('podcastcategory', models.ForeignKey(orm[u'podcasts.podcastcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['podcast_id', 'podcastcategory_id'])

        # Adding model 'PodcastCategory'
        db.create_table(u'podcasts_podcastcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['podcasts.PodcastCategory'], null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'podcasts', ['PodcastCategory'])

        # Adding model 'PodcastEpisode'
        db.create_table(u'podcasts_podcastepisode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('image_href', self.gf('django.db.models.fields.URLField')(max_length=2000)),
            ('enclosure', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['podcasts.PodcastEnclosure'], unique=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(default='pe:332bfbd3-8708-4b52-9484-0f636c4f1251', max_length=255)),
            ('pubDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('explicit', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'podcasts', ['PodcastEpisode'])

        # Adding model 'PodcastEnclosure'
        db.create_table(u'podcasts_podcastenclosure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2000)),
            ('length', self.gf('django.db.models.fields.IntegerField')(max_length=16)),
            ('type', self.gf('django.db.models.fields.CharField')(default='audio/mpeg', max_length=255)),
        ))
        db.send_create_signal(u'podcasts', ['PodcastEnclosure'])


    def backwards(self, orm):
        # Deleting model 'Podcast'
        db.delete_table(u'podcasts_podcast')

        # Removing M2M table for field categories on 'Podcast'
        db.delete_table(db.shorten_name(u'podcasts_podcast_categories'))

        # Deleting model 'PodcastCategory'
        db.delete_table(u'podcasts_podcastcategory')

        # Deleting model 'PodcastEpisode'
        db.delete_table(u'podcasts_podcastepisode')

        # Deleting model 'PodcastEnclosure'
        db.delete_table(u'podcasts_podcastenclosure')


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
            'guid': ('django.db.models.fields.CharField', [], {'default': "'pe:931e11c5-4a65-48b2-99e8-9adbcabe6804'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_href': ('django.db.models.fields.URLField', [], {'max_length': '2000'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['podcasts']