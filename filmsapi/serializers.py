from rest_framework import serializers
from .models import Movies,Actors,MoviesActors

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields='__all__'
        
class MoviesSerializer(serializers.ModelSerializer):
    # actors=serializers.StringRelatedField(many=True)
   
    class Meta:
        model=Movies
        fields='__all__'
 
class MoviesActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MoviesActors
        fields='__all__'
        
        
def create(self,validated_data):     
    data = validated_data('actors')
    data = validated_data('movies')
    
    Movies = Movies.objects.create(**validated_data)
    for actors_data in actors_data:
            actors= Actors.objects.get_or_create(**actors_data)
            MoviesActors.objects.create(movies=Movies, actors=Actors)
    return Movies.objects.create(**validated_data)

def update(self, instance, validated_data):
     instance.id = validated_data.get('id', instance.id)
     instance.movies_name = validated_data.get('movies_name', instance.movies_name)
     instance.actors = validated_data.get('actors', instance.actors)
     instance.save()
     return instance
                 


