import requests
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status


class FilmSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    original_title = serializers.CharField()
    original_title_romanised = serializers.CharField()
    image = serializers.CharField()
    movie_banner = serializers.CharField()
    description = serializers.CharField()
    director = serializers.CharField()
    producer = serializers.CharField()
    release_date = serializers.CharField()
    running_time = serializers.CharField()
    rt_score = serializers.CharField()
    url = serializers.CharField()
    
    species = serializers.ListField()
    locations = serializers.ListField()
    vehicles = serializers.ListField()
    people = serializers.ListField()


@api_view(['GET'])
@renderer_classes([renderers.JSONRenderer])
def get_films(request):
    print(request.GET['API-KEY'])
    url = 'https://ghibli.rest/films'
    films = requests.get(url)
    response = FilmSerializer(data=films.json(), many=True)
    response.is_valid(raise_exception=True)
    return Response(data=response.data, status=status.HTTP_200_OK)

