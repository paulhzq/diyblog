from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('Author')
    post_date =models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    comment_post = models.ForeignKey('Post')
    author = models.ForeignKey(User)

    def __str__(self):
        return self.content

class Author(models.Model):
    firstname = models.CharField(max_length=36)
    lastname = models.CharField(max_length=36)
    bio = models.TextField()

    def __str__(self):
        return self.firstname + ' '  + self.lastname
