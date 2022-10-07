from django.shortcuts import render

# Create your views here.
def main(request):

  return render(request, 'movies/main.html')

def index(request):

  return render(request, 'movies/index.html')

def create(request):

  return render(request, 'movies/create.html')