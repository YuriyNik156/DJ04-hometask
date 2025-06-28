from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.utils.timezone import now

def add_movie(request):
    error = ""
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
        else:
            error = "Данные введены некорректно"
    else:
        form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form, 'error':error, 'now': now()})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'films/movie_list.html', {'movies': movies})