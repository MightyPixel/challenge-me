from django.db import models
from django.contrib.auth.models import User
 

class Support(models.Model):
    supported_on = models.DateTimeField(auto_now_add=True)
    challenge = models.ForeignKey('challenges.Challenge')
    supporter = models.ForeignKey(User)
    value = models.FloatField()

    def get_absolute_url(self):
        return "/supports/support/%i/" % self.id
