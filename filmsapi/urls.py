from django.urls import path
from filmsapi import views

urlpatterns = [
    path('movies/', views.Movies_list.as_view()),
    path('actors/', views.Actors_list.as_view()),
    # path('filmsapi/', views.Movies_details),
    
    path('movies/<int:id>/', views.Movies_details.as_view()),
]