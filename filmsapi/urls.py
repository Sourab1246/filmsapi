from django.urls import path
from filmsapi import views

urlpatterns = [
    path('filmsapi/', views.Movies_list),
    path('apis/', views.Actors_list),
    # path('filmsapi/', views.Movies_details),
    
    path('Movies/<int:id>/', views.MoviesActors_details),
]