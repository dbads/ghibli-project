from django.urls import path
from .views import get_film

urlpatterns = [
    path('', get_film, name='film'),
]