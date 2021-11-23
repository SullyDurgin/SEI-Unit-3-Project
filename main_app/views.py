from django.shortcuts import render
from .models import Author, Topic, Post


def home(request):
    return render(request, 'base.html')

def detail(request, slug):
    return render(request, "detail.html", {})

def forum(request):
    return render(request, "forums.html", {})

def post(request):
    return render(request, "posts/posts.html", {})
