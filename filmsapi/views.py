from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from .models import Actors,Movies,MoviesActors
from filmsapi.serializers import ActorsSerializer,MoviesSerializer,MoviesActorsSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET','POST'])
def Movies_list (request):
        
        if request.method=='GET':
            filmsapi=Movies.objects.all()
            serializer=MoviesSerializer(filmsapi,many=True)
            return JsonResponse(serializer.data,safe=False)
    
    
  
        elif request.method=='POST': 
            # data=JSONParser().parse(request)
            serializer=MoviesSerializer(data=request.data)
            if serializer.is_valid():
              serializer.save()
              return JsonResponse(serializer.data,status=201)
            return JsonResponse(serializer.errors,status=400)
# actors_list
@api_view(['GET','POST'])
def Actors_list (request):
    if request.method=='GET':
       apis=Actors.objects.all()
       serializer=ActorsSerializer(apis,many=True)
       return JsonResponse(serializer.data,safe=False)
  
    elif request.method=='POST':
        # data=JSONParser().parse(request)
        apis=Actors.objects.all()
        serializer=ActorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.data,status=400)

@api_view(['GET','POST','DELETE'])
def MoviesActors_details(request,id):
    try:
        movies=Movies.objects.all(id=id)
       
    except Movies.DoesnotExist:
       return JsonResponse(status=404)
   
    if request.method=='GET':
        serializer=MoviesActorsSerializer([Movies,Actors,MoviesActors])
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=MoviesActorsSerializer([Movies,Actors,MoviesActors],data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        Movies.delete()
        return JsonResponse(status=204)
