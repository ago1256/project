from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets={
            "title":TextInput(attrs={
                'class':"form-control",
                'placeholder':"Название статьи"
            }),
            "anons":TextInput(attrs={
                'class':"form-control",
                'placeholder':"Анонс"
            }),
            "date":DateTimeInput(attrs={
                'class':"form-control",
                'placeholder':"Дата публикации"
            }),
            "full_text":TextInput(attrs={
                'class':"form-control",
                'placeholder':"Текст статьи"
            })
        }