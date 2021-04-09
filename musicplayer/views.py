# import module
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Song, Album, AlbumSong
from django.contrib import messages
from django.db.models import Q

# view Function.
def home(request):
   
    # define null dictionary 
    data = dict()
    # check request get or post
    if request.method == "POST":

        # filter data with movie name column
        data["movie"] = Movie.objects.filter(Q(movie_name__icontains=request.POST.get("s")))

    else:
        # All movie data fetch
        data["movie"] = Movie.objects.all()

    # return html file & also pass data
    return render(request, "movie.html", context=data)


def album_list(request):
    # define null dictionary
    data = dict()
    # check request get or post
    if request.method == "POST":
        # filter data with album name column
        data["movie"] = Album.objects.filter(Q(album_name__icontains=request.POST.get("s")))
    else:
        # All album data fetch
        data["movie"] = Album.objects.all()
    # return html file & also pass data
    return render(request, "album.html", context=data)


def album_song(request, pk):
    # define null dictionary
    data = dict()
    album_name = Album.objects.get(pk=pk).album_name
    # dynamic url pk fetch in parameter & filter album song album wise.
    song = AlbumSong.objects.filter(album_id_id=pk)
    data["song"] = song
    data["name"] = album_name
    # return html file & also pass data
    return render(request, "album-song.html", context=data)


def song(request, pk):
    # define null dictionary
    data = dict()
    movie_name = Movie.objects.get(pk=pk).movie_name
    print("*** ", movie_name)
    # Song filter movie wise.
    song = Song.objects.filter(movie_id_id=pk)
    data["song"] = song
    data["name"] = movie_name
    # return html file & also pass data
    return render(request, "song.html", context=data)


def song_play(request, pk):
    # define null dictionary
    data = dict()
    # Song filter
    song = Song.objects.get(pk=pk)
    data["song"] = song

    # return html file & also pass data
    return render(request, "play.html", context=data)


def album_song_play(request, pk):
    # define null dictionary
    data = dict()
    # Filter song 
    song = AlbumSong.objects.get(pk=pk)
    data["song"] = song
    # return html file & also pass data
    return render(request, "album-play.html", context=data)


def detail(request):
    return render(request, "home.html")

def mvt(request):
    return render(request, "mvt.html")