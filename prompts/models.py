from django.db import models
from django.contrib.auth.models import User


class Morning(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    great = models.TextField(verbose_name='What would make today great?')
    grateful = models.TextField(verbose_name='I am grateful for:')
    affirmation = models.TextField(verbose_name='Daily affirmations: I am...')

    def __str__(self):
        return "{0} m [{1}]".format(self.pub_date.strftime('%Y-%m-%d'), self.author.username[:1])

    class Meta:
        ordering = ['-pub_date']


class Evening(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    three_things = models.TextField(verbose_name="3 amazing things that happened today:")
    improve = models.TextField(verbose_name="How could I have made today better?")
    plan = models.TextField(verbose_name="MIT and other plans for tomorrow:")

    def __str__(self):
        return "{0} e [{1}]".format(self.pub_date.strftime('%Y-%m-%d'), self.author.username[:1])

    class Meta:
        ordering = ['-pub_date']