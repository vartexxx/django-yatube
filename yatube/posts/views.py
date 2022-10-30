from django.shortcuts import render
from .models import Post

def index(request):
    template = 'posts/index.html'
    title = 'Главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)