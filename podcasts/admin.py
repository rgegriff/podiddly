from django.contrib import admin
from models import *

class PodcastAdmin(admin.ModelAdmin):
    pass

class PodcastEpisodeAdmin(admin.ModelAdmin):
    pass

class PodcastCategoryAdmin(admin.ModelAdmin):
    pass

class PodcastEnclosureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
admin.site.register(PodcastCategory, PodcastCategoryAdmin)
admin.site.register(PodcastEnclosure, PodcastEnclosureAdmin)