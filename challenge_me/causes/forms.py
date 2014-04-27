from django.forms import ModelForm
from models import Cause, CauseComment

class CauseForm(ModelForm):
    class Meta:
        model = Cause
        fields = ['title', 'funding_goal', 'about']

class CauseCommentForm(ModelForm):
    class Meta:
        model = CauseComment
        fields = ['text']
