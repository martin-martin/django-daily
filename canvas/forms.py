from django.forms import ModelForm
from .models import Text


class TextForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'canvas', 'autofocus': 'autofocus'})

    class Meta:
        model = Text
        fields = ('text',)
