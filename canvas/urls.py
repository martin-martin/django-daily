from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Text
from .views import TextCreate, TextListView


app_name = 'canvas'

urlpatterns = [
    path('', TextCreate.as_view(), name='write'),
    path('all/', login_required(TextListView.as_view()), name='all'),
    # the path below displays all texts of all authors mixed together
    path('all/all', login_required(ListView.as_view(model=Text, context_object_name='text_list')), name='allall'),
]