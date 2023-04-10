from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from .models import Actors,Movies,MoviesActors
from filmsapi.serializers import ActorsSerializer,MoviesSerializer,MoviesActorsSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

# Create your views here.
# @api_view(['GET','POST'])
class Movies_list(APIView):
    
    def get (self,request):
        movies=Movies.objects.all()
        serializer=MoviesSerializer(movies,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        serializer=MoviesSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data ,status=201)
        return JsonResponse(serializer.errors,status=400) 
# actors_list
class Actors_list(APIView):
    def get(self,request):
        actors=Actors.objects.all()
        serializer=ActorsSerializer(actors,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):   
        serializer=ActorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)
        
class Movies_details(APIView):
    def get_object(self,id):
        try:
            return Movies.objects.get(id=id)       
        except Movies.DoesNotExist:
            return JsonResponse(staus=404)
        
    def get(self,request,id):
        movies= self.get_object(id)  
        serializer=MoviesSerializer(movies)
        return JsonResponse(serializer.data)
    def put(self,request,id):
        movies= self.get_object(id)  
        serializer=MoviesSerializer(movies,data=request.data)
        if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400) 
    def delete(self,request,id):
        movies=self.get_objects.get(id)    
        movies.delete()
        return JsonResponse(status=204)
       
        
        
    
