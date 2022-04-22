from django.contrib import admin

from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') 
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description') 
    search_fields = ('title', 'slug', 'description',) 
    list_filter = ('title', 'slug') 
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin) 
admin.site.register(Group, GroupAdmin)