from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Album, Songs
from user.models import Profile
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

class FavouriteSongs(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        profile = Profile.objects.get(user = user)
        print(profile.liked_song)

        return HttpResponse(request,'Working on it.')