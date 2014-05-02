from django.db import models
import uuid

class Podcast(models.Model):
  title = models.CharField(max_length=255)
  link = models.URLField(max_length=2000)
  description = models.TextField()
  language = models.CharField(max_length=255)
  copyright = models.CharField(max_length=255)
  pubdate = models.DateTimeField(auto_now_add=True)
  subtitle = models.CharField(max_length=255, null=True, blank=True)
  summary = models.CharField(max_length=4000, null=True, blank=True)
  author = models.CharField(max_length=255, null=True, blank=True)
  owner_name = models.CharField(max_length=255, null=True, blank=True)
  owner_email = models.CharField(max_length=255, null=True, blank=True)
  image_href = models.URLField(max_length=255, null=True, blank=True)
  categories = models.ManyToManyField("PodcastCategory", null=True, blank=True)
  explicit = models.BooleanField()
  
class PodcastCategory(models.Model):
  parent = models.ForeignKey("PodcastCategory", null=True, blank=True)
  text = models.CharField(max_length=255)
  
class PodcastEpisode(models.Model):
  podcast = models.ForeignKey("Podcast")
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255)
  summary = models.TextField()
  image_href = models.URLField(max_length=2000)
  enclosure = models.OneToOneField("PodcastEnclosure")
  guid = models.CharField(max_length=255, default=lambda: "pe:%s"%uuid.uuid4())
  pubDate = models.DateTimeField(auto_now_add=True)
  explicit = models.BooleanField()
  
class PodcastEnclosure(models.Model):
  TYPES_AVAILABLE=(('.mp3',	'audio/mpeg'),
                   ('.m4a',	'audio/x-m4a'),
                   ('.mp4',	'video/mp4'),
                   ('.m4v',	'video/x-m4v'),
                   ('.mov',	'video/quicktime'),
                   ('.pdf',	'application/pdf'),
                   ('.epub', 'document/x-epub'))

  url = models.URLField(max_length=2000)
  length = models.IntegerField(max_length=16)#length in bytes
  type = models.CharField(max_length=255, default="audio/mpeg")