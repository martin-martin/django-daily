from django.urls import path
from .views import write


urlpatterns = [
    path('', write),  # could be 'canvas/'
]