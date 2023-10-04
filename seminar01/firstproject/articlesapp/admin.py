from django.contrib import admin
from .models import Author, Article, Comment

# регистрируем модели в админке
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)


