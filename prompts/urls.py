from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Morning, Evening
from .views import CreateMorningView, CreateEveningView, ShowMorningList, ShowEveningList


app_name = 'prompts'

urlpatterns = [
    path('morning', login_required(CreateMorningView.as_view()), name='morning'),
    path('evening', login_required(CreateEveningView.as_view()), name='evening'),
    path('m', login_required(ShowMorningList.as_view()), name='morning_list'),
    path('e', login_required(ShowEveningList.as_view()), name='evening_list'),
    # the paths below display all texts of all authors mixed together
    path('m/all', login_required(ListView.as_view(model=Morning)), name='morning_list_all'),
    path('e/all', login_required(ListView.as_view(model=Evening)), name='evening_list_all'),
]