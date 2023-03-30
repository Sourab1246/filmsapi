from django.urls import path, include
from rest_framework import routers
from .views import Movies_list, Actors_list,Movies_details,Movies


router = routers.DefaultRouter()
# router.register(r'Actors',Actors_list, basename='Actors_list' )
# router.register(r'Movies', Movies_list, basename='Movies_list')
# # router.register(r'Movies', Movies_details, basename='Movies')




urlpatterns = [
    path('', include(router.urls)),
    # path('Movies_details/', Movies),
    
]