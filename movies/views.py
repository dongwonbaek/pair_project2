from django.shortcuts import render, redirect
from movies.forms import MovieForm
from .models import Movie

# Create your views here.
def main(request):

  return render(request, 'movies/main.html')

def index(request):
  movie = Movie.objects.all()
  context = {
    'movies':movie,
  }

  return render(request, 'movies/index.html', context)

def detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  context={
    'movie':movie,
  }
  return render(request, 'movies/detail.html', context)

def create(request):
  if request.method == 'POST':
    movies = MovieForm(request.POST)
    if movies.is_valid():
      movie_detail = movies.save()
      return redirect('movies:detail', movie_detail.pk)
  else:
    movies = MovieForm()
  context = {
    'movies': movies,
  }
  return render(request, 'movies/create.html', context)

def update(request, pk):
  movie = Movie.objects.get(pk=pk)
  if request.method == 'POST':
    movies = MovieForm(request.POST, instance=movie)
    if movies.is_valid():
      movie_detail = movies.save()
      return redirect('movies:detail', movie_detail.pk)
  else:
    movies = MovieForm(instance=movie)
  context = {
    'movie': movie,
    'movies': movies,
  }
  return render(request, 'movies/update.html', context)
