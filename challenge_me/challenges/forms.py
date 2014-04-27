from django.forms import ModelForm
from models import Challenge, ChallengeComment

class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['deadline', 'goal']

class ChallengeCommentForm(ModelForm):
    class Meta:
        model = ChallengeComment 
        fields = ['text']
