from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView
from .models import Text


class TextCreate(LoginRequiredMixin, CreateView):
    model = Text
    fields = ['text']
    template_name = 'canvas/canvas.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TextCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('canvas:all')


class TextListView(LoginRequiredMixin, ListView):
    """Displays the 7 most recent '750-words'-entries written by the logged-in user."""
    model = Text
    template_name = 'canvas/text_list.html'
    context_object_name = 'text_list'

    def get_queryset(self):
        return Text.objects.filter(author=self.request.user)[:7]
