from django import forms
from .models import Profile,Project,Comment
from django.contrib.auth.models import User
from django.forms import ModelForm


class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','project']
