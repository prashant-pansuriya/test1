# import module
from django.db import models

# Create your models here.

# Define Model Class
class Movie(models.Model):
    
    # Define Model Field
    movie_name = models.CharField(max_length=200, unique=True)
    movie_type = models.CharField(max_length=100)
    movie_img = models.ImageField(upload_to="media/mov-img/")
    year = models.IntegerField()
    
    
    def __str__(self):
        return self.movie_name

# Define Model Class
class Song(models.Model):
    
    # Define Model Field
    name = models.CharField(max_length=200)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    song_img = models.ImageField(upload_to="media/song-img/")
    # singer = models.CharField(max_length=200)
    song_file = models.FileField("media/")

    class Meta:
        unique_together = ('name', 'movie_id')

    def __str__(self):
        return self.name

# Define Model Class
class Album(models.Model):

    # Define Model Field
    album_name = models.CharField(max_length=200, unique=True)
    album_img = models.ImageField(upload_to="media/mov-img/")
    year = models.IntegerField()

    def __str__(self):
        return self.album_name

# Define Model Class
class AlbumSong(models.Model):
    
    # Define Model Field
    name = models.CharField(max_length=200)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_img = models.ImageField(upload_to="media/song-img/")
    # singer = models.CharField(max_length=200)
    song_file = models.FileField("media/")

    # Class Meta property define
    class Meta:
        unique_together = ('name', 'album_id')

    def __str__(self):
        return self.name

