from django.db import models
from django.contrib.auth.models import User


class Cause(models.Model):
    funding_goal = models.FloatField()
    title = models.CharField(max_length=255)
    about = models.TextField()

    def get_absolute_url(self):
        return "/causes/cause/%i/" % self.id


class CauseComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    cause = models.ForeignKey(Cause)
