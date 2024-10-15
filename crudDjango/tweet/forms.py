from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo'] # fields to display in the form
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'What\'s happening?'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }