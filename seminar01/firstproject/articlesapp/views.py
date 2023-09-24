from django.shortcuts import render, get_object_or_404
from articlesapp.models import Author, Article, Comment
from articlesapp.forms import AuthorForms, AddArticle, AddComment

import logging

logger = logging.getLogger(__name__)


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
    """form to add a commentaryby author"""

    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    article.views += 1
    article.save()
    comments = Comment.objects.filter(article=article).all()
    context = {
        'article': article,
        'author': author,
        'comments': comments,
        'form': AddComment,
        'button': 'Publish',
    }

    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            author_pk = int(form.cleaned_data['author_pk'])
            c_author = get_object_or_404(Author, pk=author_pk)
            c_article = get_object_or_404(Article, pk=article_id)
            Comment(
                author=c_author,
                article=c_article,
                text=content,
            ).save()

    return render(request, template_name='articlesapp/article.html', context=context)


def add_author(request):
    if request.method == 'POST':
        form = AuthorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            biography = form.cleaned_data.get('biography')
            birthday = form.cleaned_data.get('birthday')
            print(f'GET {name} {surname} {email} {biography} {birthday}')
    else:
        form = AuthorForms()
    return render(request=request, template_name='articlesapp/author_form.html', context={'form': form})


def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            article = Article(
                title=title,
                content=content,
                author=author,
                category=category,
            )
            article.save()
            logger.info(f'Added article: {article}')
            print(f'Added article: {article}')
    else:
        logger.info(f'Adding article')
        form = AddArticle()
    return render(request, template_name='articlesapp/article_form.html',
                  context={'form': form, 'title': 'Add article', 'button': 'Add article'})
