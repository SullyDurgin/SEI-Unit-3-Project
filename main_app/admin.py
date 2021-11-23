from django.contrib import admin
from .models import Topic, Author, Post

admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Post)
