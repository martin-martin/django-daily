from django.shortcuts import render
from django.views.generic import CreateView
from .models import Morning, Evening


class MorningView(CreateView):
    model = Morning
    fields = ['great', 'grateful', 'affirmation']
    template_name = 'prompts/morning.html'


class EveningView(CreateView):
    model = Evening
    fields = ['three_things', 'improve', 'plan']
    template_name = 'prompts/evening.html'
