"""Хранение представлений (контролеров) текущего приложения
Posts
"""
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Group, Post, User


def index(request):
    """Функция представления главной страницы проекта
    Yatube, с учётом сортировки количества постов для
    текущего приложения
    """
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.CONST_1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
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

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    count = author.posts.count()
    paginator = Paginator(posts, settings.CONST_1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/post_profile.html'
    context = {
        'page_obj': page_obj,
        'count': count,
        'author': author,
    }
    return render(request, template, context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    title = post.text[:settings.CONST_2]
    pub_date = post.pub_date
    author = post.author
    author_posts = author.posts.all().count()
    template = 'posts/post_detail.html'
    context = {
        'author': author,
        'author_posts': author_posts,
        'post': post,
        'title': title,
        'pub_date': pub_date,
    }
    return render(request, template, context)