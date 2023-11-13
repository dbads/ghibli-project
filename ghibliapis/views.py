# python core modules imports
import requests

# django imports
from django.core.cache import cache
from django.conf import settings

# drf imports
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import status

# custom imports
from .serializers import FilmSerializer

CACHE_TIMEOUT_FOR_FILMS = 60

"""
    gets the film data, serializes them, checks for validity of different properties
"""
def prepare_response_from_data(data):
    response = FilmSerializer(data=data)
    response.is_valid(raise_exception=True)

    return response.data


"""
    prepare actors data
    checking if actor already in cache then use that data, else fetch actor and set in cache
"""
def prepare_actors_data(people_urls: list[str]) -> list:
    actors = []
    for people_url in people_urls:
        actor_id = people_url.split("=")[1]
        actor_data = cache.get(actor_id)
        if actor_data:
            actors.append(actor_data)
        else:
            actor_data = requests.get(people_url).json()
            cache.set(actor_id, actor_data[0], CACHE_TIMEOUT_FOR_FILMS)
            actors.append(actor_data[0])
    
    return actors


"""
    Get Film method get film id from request and returns the film data
    An API_KEY is must to get film data, otherwise it will throw a 403 response
"""
@api_view(['GET'])
@renderer_classes([renderers.JSONRenderer])
def get_film(request):
    API_KEY = request.GET.get('API-KEY')
    film_id = request.GET.get('id')
    url = f'https://ghibli.rest/films?id={film_id}'

    film_data_from_redis = cache.get(film_id)
    
    # check if data already in cache, then return the same
    if film_data_from_redis:
        response_data = prepare_response_from_data(film_data_from_redis)
        return response_data
    else:
        # if data not in cache then fetch it and set in cache

        # API_KEY validation
        if API_KEY is None or API_KEY != settings.API_KEY:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)
        
        # fetch film data
        film_data = requests.get(url)

        # check if data was found on the server
        if film_data:
            film_data = film_data.json()[0]
        else:
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)

        # prepare actors
        actors = prepare_actors_data(film_data['people'])

        # remove people from film data and add actors
        del film_data['people']
        film_data['actors'] = actors

        # setting film data in cache for 1 minutes
        cache.set(film_id, film_data, CACHE_TIMEOUT_FOR_FILMS)

        # prepare and send response
        response_data = prepare_response_from_data(film_data)
        return Response(data=response_data, status=status.HTTP_200_OK)

