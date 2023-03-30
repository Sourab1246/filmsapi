from django.urls import path
from .views import Actors_list,Movies_list,Movies_details
from apis import views

urlpatterns = [
    path('Movies/',views.Movies_list()),
    path('Actors/',views.Actors_list()),
    # path('/',Actors_list.as_view()),
    
]   
    
    
    
    
    

