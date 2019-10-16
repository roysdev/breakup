from django import forms
from .models import Comment
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comment
        fields = ('text',)
