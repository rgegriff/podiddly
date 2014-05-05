from django.db import models
import datetime
from feedgen.feed import FeedGenerator
import uuid

class Podcast(models.Model):
  MAPPINGS = (
      (("title",),("title",)),
      (("link_dict",),("link",)),
      (("description",),("description",)),
      (("language",),("language",)),
      (("copyright",),("rights",)),
      (("pubdate",),('pubDate',)),
      (("subtitle",),('podcast', 'itunes_subtitle',)),
      (("summary",),("podcast", "itunes_summary",)),
      (("author",),("podcast", "itunes_author",)),
      (("owner_name", "owner_email"),("podcast", "itunes_owner",)),
      (("image_href",), ("podcast", "itunes_image",)),
      (("itunes_explicit",), ("podcast", "itunes_explicit",))
    )

  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255)
  link = models.URLField(max_length=2000)
  link_rel = models.CharField(max_length=255, default="self")
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

  @property
  def link_dict(self):
    return {"href":self.link, "rel":self.link_rel}

  @property
  def itunes_explicit(self):
    # @todo: make this support clean setting as well
    return "yes" if self.explicit else "no"

  def generate_feed(self):
    fg = FeedGenerator()
    fg.load_extension('podcast')
    for field in self.MAPPINGS:
      value_names = field[0]
      methods = field[1]
      
      values = []
      # collect the values from self
      for value_name in value_names:
        values.append( getattr(self, value_name) )
      
      method = fg
      # decend the attribute tree
      for m_part in methods:
        method = getattr(method, m_part)
      # apply the values to the found method
      print m_part, values
      method(*values)

    return fg.rss_str(pretty=True)
          

  def __unicode__(self):
    return self.title
  
class PodcastCategory(models.Model):
  parent = models.ForeignKey("PodcastCategory", null=True, blank=True)
  text = models.CharField(max_length=255)
  
  def __unicode__(self):
    out = ""
    if parent is not None:
      out = "%s > "%parent.name
    out += self.title
    return out
  
class PodcastEpisode(models.Model):
  class Meta:
    ordering = ["-pubdate"]

  podcast = models.ForeignKey("Podcast", related_name="episodes")
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255)
  summary = models.TextField()
  image_href = models.URLField(max_length=2000)
  enclosure = models.OneToOneField("PodcastEnclosure")
  guid = models.CharField(max_length=255, default=lambda: "pe:%s"%uuid.uuid4())
  pubdate = models.DateTimeField(auto_now_add=True, default=lambda:datetime.datetime.now())
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
    
