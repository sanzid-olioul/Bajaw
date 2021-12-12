from django.shortcuts import render
from django.views import View
from .models import Album, Songs
# Create your views here.
class SongsList(View):
    def get(self,request,*args,**kwargs):
        songs = Songs.objects.all()
        return render(request,'music/song_list.html',{'songs':songs})

class PlaySong(View):
    def get(self,request,*args,**kwargs):
        song = Songs.objects.get(pk=kwargs['id'])
        
        print(song.album.album_name)
        return render(request,'music/play_song.html',{'song':song})