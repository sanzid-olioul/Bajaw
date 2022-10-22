from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SongsList,PlaySong,FavouriteSongs


urlpatterns = [
    path('music/', login_required(SongsList.as_view(),login_url='user_login'), name = 'music_list'),
    path('music/<int:id>/', login_required(PlaySong.as_view(),login_url='user_login'), name = 'play_music'),
    path('user/favourite/', login_required(FavouriteSongs.as_view(),login_url='user_login'), name = 'favoutire_songs'),
]
