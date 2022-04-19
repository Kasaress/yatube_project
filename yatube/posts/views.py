from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    return HttpResponse('Главная страница, самая главная')


# Страница с постами, отфильтрованными по группам 
def group_posts(request, slug):
    return HttpResponse('Посты')    
