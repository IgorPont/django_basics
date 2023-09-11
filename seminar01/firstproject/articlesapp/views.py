from django.shortcuts import render, get_object_or_404
from articlesapp.models import Author, Article, Comment


def get_articles_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    article = Article.objects.filter(author=author)

    context = {
        'title': 'Статьи автора',
        'author': author,
        'articles': article,
    }
    return render(request, template_name='articlesapp/articles.html', context=context)


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # author = article.author
    comments = Comment.objects.filter(article=article)

    context = {
        'title': article.title,
        'article': article,
        'comments': comments,
    }
    return render(request, template_name='articlesapp/article.html', context=context)
