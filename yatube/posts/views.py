from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


# Страница с постами, отфильтрованными по группам 
def group_posts(request, slug): 
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        }
    return render(request, template, context)  
