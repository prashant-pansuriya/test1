"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import module
from django.urls import path
from .views import home, song, song_play, detail, album_list, album_song, album_song_play, mvt

# define url 

urlpatterns = [
    # path("url name", "function name", "name")
    path('', detail, name="Studnet-detail"),
    path('movie', home, name="movie-song-list"),
    path('song-all/<pk>', song, name="song"),
    path('song-play/<pk>', song_play, name="song-play"),
    path('album', album_list, name="album"),
    path('album-all/<pk>', album_song, name="album"),
    path('album-song-play/<pk>', album_song_play, name="album-song"),
    path('mvt', mvt, name="mvt"),
]





