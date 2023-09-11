from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField()
    birthday = models.DateField()

    def get_fullname(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.published} {self.public_date}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment for atricle "{self.article.title}", author: {self.author.get_fullname}'
