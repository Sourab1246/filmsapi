from rest_framework import serializers
from apis.models import Movies,Actors,MoviesActors

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        models=Actors
        fields='__all__'
        
class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        models=Movies
        fields='__all__'     
        
def create(self,validated_data):     
    # actors_data = validated_data.pop('actors')
    # movies = Movies.objects.create(**validated_data)
    # for actors_data in actors_data:
    #         actors= Actors.objects.get_or_create(**actors_data)
    #         MoviesActors.objects.create(movies=movies, actors=actors)
    return Movies.object.create(**validated_data)
