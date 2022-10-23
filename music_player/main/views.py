from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Album, Song

# Create your views here.
class SongsList(View):
    '''
    For passing all the songs list
    '''
    def get(self,request,*args,**kwargs):
        songs = Song.objects.all()
        return render(request,'music/song_list.html',{'songs':songs})

class PlaySong(View):
    '''
    Playing a perticular song
    '''
    def get(self,request,*args,**kwargs):
        song = Song.objects.get(pk=kwargs['id'])
        
        print(song.album.album_name)
        return render(request,'music/play_song.html',{'song':song})

class FavouriteSongs(View):
    '''
    User favourite song will be send
    '''
    def get(self,request,*args,**kwargs):
        user = request.user
        songs = Song.objects.filter(liked_by = user)

        return render(request,'music/song_list.html',{'songs':songs})