from django.contrib import admin
from .models import Movie, Song, Album, AlbumSong
# Register your models here.
# Show data table in admin panel
admin.site.register(Movie)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(AlbumSong)

