from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Forum, Posts
from .forms import PostsForm


S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = "forum-collector-bucket-of-fun"


class Home(LoginView):
    template_name = 'home.html'


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
    post_form = PostsForm()
    return render(request, 'forums/detail.html', {
        'forum': forum, 'post_form': post_form
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
    return redirect("forums_detail", forum_id=forum_id)


class PostCreate(CreateView):
    model = Posts
    fields = ['date', 'title', 'author', 'date',
              'comment', 'topic', 'spookyLevel', 'description']
    


class PostList(ListView):
    model = Posts


class PostDetail(DetailView):
    model = Posts


class PostUpdate(UpdateView):
    model = Posts
    fields = ['date', 'title', 'author', 'date',
              'comment', 'topic', 'spookyLevel']


class PostDelete(DeleteView):
    model = Posts
    success_url = '/posts/'
