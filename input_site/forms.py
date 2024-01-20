from django import forms

from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'text']
        labels = {'text':''}

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['text']
        labels = {'text': 'comment:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
