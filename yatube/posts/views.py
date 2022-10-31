"""Хранение представлений (контролеров) текущего приложения
Posts
"""
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Функция представления главной страницы проекта
    Yatube, с учётом сортировки количества постов для
    текущего приложения
    """
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.all()[:settings.CONST_1]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Функция представления страницы групп для проекта
    Yatube, с учётом сортировки количества постов для
    текущего приложения
    """
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:settings.CONST_1]
    template = 'posts/group_list.html'
    group_title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group_title': group_title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
