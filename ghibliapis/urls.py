from django.urls import path
from .views import get_films

urlpatterns = [
    path('', get_films),
]