from django.contrib import admin

# Register your models here.
from .models import Song,Album,Singer
@admin.register(Song)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['song_name','extension','music_file','duration']
@admin.register(Album)
class AmbumAdmin(admin.ModelAdmin):
    list_display = ['album_name','image','get_singers']
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
     list_display = ['singer_name','image','about']