from django.urls import path
from .views import MorningView, EveningView


app_name = 'prompts'

urlpatterns = [
    path('morning', MorningView.as_view(), name='morning'),
    path('evening', EveningView.as_view(), name='evening'),
]