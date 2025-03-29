from django import forms
from .models import TweetMessage

class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetMessage
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'textarea textarea-bordered w-full h-32',
                'placeholder': "What's happening?",
                'x-data': '',
                'x-ref': 'tweetTextarea',
                '@input': 'updateCounter()'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.pk:  # Only set author for new tweets
            instance.author = self.user
        if commit:
            instance.save()
        return instance
