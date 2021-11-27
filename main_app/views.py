from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Forum
from .forms import PostsForm


S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = "forum-collector-bucket-of-fun"


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def forums_index(request):
    forums = Forum.objects.all()
    # similar to forum.find({}) in MEN stack
    return render(request, 'forums/index.html', {'forums': forums})


def forums_detail(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    posts_form = PostsForm()
    return render(request, 'forums/detail.html', {
        'forum': forum, 'posts_form': posts_form
    })


class ForumCreate(CreateView):
    model = Forum
    fields = ['title', 'author', 'comment', 'spookyLevel']


class ForumUpdate(UpdateView):
    model = Forum
    fields = ['author', 'comment', 'spookyLevel']


class ForumDelete(DeleteView):
    model = Forum
    success_url = '/forums/'


def add_posts(request, forum_id):
    form = PostsForm(request.POST)
    if form.is_valid():
        new_posts = form.save(commit=False)
        new_posts.forum_id = forum_id
        new_posts.save()
    return redirect("Forums_detail", forum_id=forum_id)
