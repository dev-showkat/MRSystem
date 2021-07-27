from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Movie(models.Model):
	title   	= models.CharField(max_length=200)
	movie_logo  = models.FileField() 

	def __str__(self):
		return self.title

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE) 
	movie 	= models.ForeignKey(Movie,on_delete=models.CASCADE)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
		

genre_choices = [
		('action', 'action'),
		('adventure', 'adventure'),
		('animation', 'animation'),
		('biography', 'biography'),
		('comedy', 'comedy'),
		('crime', 'crime'),
		('drama', 'drama'),
		('family', 'family'),
		('fantasy', 'fantasy'),
		('horror', 'horror'),
		('mystery', 'mystery'),
		('romance', 'romance'),
		('thriller', 'thriller'),
		('war', 'war'),
		
	]
class Genre(models.Model):
	genre = models.CharField(max_length=16, choices=genre_choices )
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
