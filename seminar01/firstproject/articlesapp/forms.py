from django import forms
from articlesapp.models import Author, Article, Comment


class AuthorForms(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField()


class AddArticle(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)


class AddComment(forms.Form):
    """Add a new commentary by author to a database"""

    authors = [(f'{author.pk}', f'{author.surname} {author.name}')
               for author in Author.objects.all()]
    author_pk = forms.ChoiceField(choices=authors)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


