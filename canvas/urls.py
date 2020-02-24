from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Text
from .views import write


app_name = 'canvas'

urlpatterns = [
    path('', write, name='canvas'),  # could be 'canvas/'
    path('all/', login_required(ListView.as_view(model=Text))),
]