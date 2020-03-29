from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
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
