from rest_framework import serializers

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
    
    # list fields
    species = serializers.ListField()
    locations = serializers.ListField()
    vehicles = serializers.ListField()
    people = serializers.ListField(required=False)
    actors = serializers.ListField()