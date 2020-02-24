from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(help_text="Here goes the content of your mind today.")

    def __str__(self):
        return "{0} - {1}... {2}".format(self.pub_date.strftime('%Y-%m-%d (%a) %H:%M'), self.text[:30], self.author)

    class Meta:
        ordering = ['-pub_date']
