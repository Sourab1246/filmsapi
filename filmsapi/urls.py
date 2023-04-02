from django.urls import path
from filmsapi import views

urlpatterns = [
    path('filmsapi/', views.Movies_list),
    path('filmsapi/', views.Actors_list),
    path('filmsapi/', views.Movies_details),
    
    path('filmsapi/<int:pk>/Movieslist', views.Movies_details),
]