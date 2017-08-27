from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000,help_text='Enter your blog text here.')
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    post_date =models.DateTimeField(default=datetime.now,blank = True)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',args=[str(self.id)])

class Comment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    content = models.TextField(max_length=1000, help_text='Enter comment about blog here.')
    date = models.DateTimeField(default=datetime.now,blank = True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        len_title=75
        if len(self.content)>len_title:
            titlestring=self.content[:len_title] + '...'
        else:
            titlestring=self.content
        return titlestring

class Author(models.Model):
    """
    Model representing a blog author.
    """

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('blogger-detail',args=[str(self.id)])
