from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news':news})

def create(request):
    error=''
    if request.method=="POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='ошибка'

    form =ArticlesForm()
    data={
        'form':form,
        'error':error
    }
    return render(request, 'news/create.html', data)