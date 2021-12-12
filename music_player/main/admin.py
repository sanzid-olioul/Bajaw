from django.contrib import admin

# Register your models here.
from .models import Songs,Album,Singer
@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['song_name','extension','music_file','duration']
@admin.register(Album)
class AmbumAdmin(admin.ModelAdmin):
    list_display = ['album_name','image','singer']
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
     list_display = ['singer_name','image','about']