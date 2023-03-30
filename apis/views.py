# from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Actors,Movies,MoviesActors
from .serializers import ActorsSerializer,MoviesSerializer
from rest_framework.parsers import JSONParser



# create views
@csrf_exempt

def Movies_list (request):
    if request.method=='GET':
        
      apis=Movies.object.all()
      serializer=MoviesSerializer(apis,many=True)
      return JsonResponse(serializer.data)
  
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=MoviesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.error,status=400)

# actors_list

def Actors_list (request):
    if request.method=='GET':
        
      apis=Actors.object.all()
      serializer=ActorsSerializer(apis,many=True)
      return JsonResponse(serializer.data)
  
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ActorsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.error,status=400)

@csrf_exempt
def Movies_details(request):
    try:
        Movies=Movies.object.all()
    except Movies.DoesnotExist:
        return JsonResponse(status=404)
    if request.method=='GET':
        serializer=MoviesSerializer(Movies)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=MoviesSerializer(Movies,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        Movies.delete()
        return JsonResponse(status=204)
    
        
    
    
    
    
         
