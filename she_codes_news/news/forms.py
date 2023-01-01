from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = [
            'title', 
            'pub_date', 
            'content', 
            'image_url',
            ]
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date',
            'type':'date'}),
        }

class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='Leave a comment')

    class Meta:
        model = Comment
        fields = ["content"]
