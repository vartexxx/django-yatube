from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)