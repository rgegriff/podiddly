from django.contrib import admin
from models import *

class PodcastAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

class PodcastAuthorAdmin(admin.ModelAdmin):
    pass

class PodcastCategoryAdmin(admin.ModelAdmin):
    pass

class PodcastEnclosureAdmin(admin.ModelAdmin):
    pass

class PodcastEpisodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastAuthor, PodcastAuthorAdmin)
admin.site.register(PodcastCategory, PodcastCategoryAdmin)
admin.site.register(PodcastEnclosure, PodcastEnclosureAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
