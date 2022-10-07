from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  movie_name = models.CharField(max_length=20)
  grade = models.IntegerField(default=10,validators=[MinValueValidator(0),MaxValueValidator(10)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  view_count = models.IntegerField(default=0)