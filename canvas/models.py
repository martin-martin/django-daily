from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(help_text="Here goes the content of your mind today.")

    def __str__(self):
        return "{0} - {1}...".format(self.pub_date, self.text[:10])

    class Meta:
        ordering = ['-pub_date']
