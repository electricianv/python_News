from django import forms
from .models import Post  # Импортируем модель Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category_type']  # Укажите здесь все поля, которые должны быть включены в форму
        labels = {
            'title': 'Заголовок',
            'text': 'Контент',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category_type']  # Укажите здесь все поля, которые должны быть включены в форму
        labels = {
            'title': 'Заголовок',
            'text': 'Контент',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

# from django import forms
# from .models import Post  # Импортируем модель Post
#
#
# class NewsForm(forms.Form):
#     title = forms.CharField(label="Заголовок", max_length=200)
#     content = forms.CharField(label="Контент", widget=forms.Textarea)
#     # ... другие поля для формы новости
#
#
# class ArticleForm(forms.Form):
#     title = forms.CharField(label="Заголовок", max_length=200)
#     content = forms.CharField(label="Контент", widget=forms.Textarea)
