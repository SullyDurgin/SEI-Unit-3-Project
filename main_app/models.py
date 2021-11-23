from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)


class Topic(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

  
class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    
