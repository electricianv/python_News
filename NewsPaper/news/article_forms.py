from django import forms
from .models import Post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].initial = 'article'
        self.fields['type'].widget = forms.HiddenInput()
