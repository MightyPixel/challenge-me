from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    cause = models.ForeignKey('causes.Cause')
    goal = models.CharField(max_length=255)
    challenger = models.ForeignKey(User)

    def get_absolute_url(self):
        return "/challenges/challenge/%i/" % self.id


class ChallengeUpdate(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    challenge = models.ForeignKey(Challenge)
    update = models.TextField()


class ChallengeProof(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    challenge = models.ForeignKey(Challenge)
    proof = models.URLField()


class ChallengeComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    update = models.CharField(max_length=1024)
    author = models.ForeignKey(User)
    text = models.CharField(max_length=1023)
    challenge = models.ForeignKey(Challenge)
