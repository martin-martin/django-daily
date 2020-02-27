from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Text
from .views import TextCreate


app_name = 'canvas'

urlpatterns = [
    path('', TextCreate.as_view(), name='write'),
    path('all/', login_required(ListView.as_view(model=Text)), name='all'),
]