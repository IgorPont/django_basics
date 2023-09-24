from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:author_id>/', views.get_articles_by_author, name='get_articles_by_author_id'),
    path('get_article/<int:article_id>/', views.get_article, name='get_article_and_add_comment'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_article/', views.add_article, name='add_article'),
]
