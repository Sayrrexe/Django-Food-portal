from django import forms
from django.core.exceptions import ValidationError

from .models import Recept, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        
