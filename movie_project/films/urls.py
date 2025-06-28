from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_movie, name='add_movie'),
    path('movies/', views.movie_list, name='movie_list'),
]
