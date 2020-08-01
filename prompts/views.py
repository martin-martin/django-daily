from django.views.generic import CreateView, ListView
from django.urls import reverse
from .models import Morning, Evening


class CreateMorningView(CreateView):
    model = Morning
    fields = ['great', 'grateful', 'affirmation']
    template_name = 'prompts/morning.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateMorningView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '... 🌤'
        return context

    def get_success_url(self):
        return reverse('prompts:morning_list')


class CreateEveningView(CreateView):
    model = Evening
    fields = ['three_things', 'improve', 'plan']
    template_name = 'prompts/evening.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateEveningView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '... 🌙'
        return context

    def get_success_url(self):
        return reverse('prompts:evening_list')


class ShowMorningList(ListView):
    """Displays all morning entries written by logged-in user."""
    model = Morning
    template_name = 'prompts/morning_list.html'

    def get_queryset(self):
        return Morning.objects.filter(author=self.request.user)


class ShowEveningList(ListView):
    """Displays all evening entries written by logged-in user."""
    model = Evening
    template_name = 'prompts/evening_list.html'

    def get_queryset(self):
        return Evening.objects.filter(author=self.request.user)
