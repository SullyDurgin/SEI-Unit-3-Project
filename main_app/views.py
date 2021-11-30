from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def forums_index(request):
    forums = Forum.objects.all()
    return render(request, 'forums/index.html', {'forums': forums})


@login_required
def forums_detail(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    post_form = PostsForm()
    return render(request, 'forums/detail.html', {
        'forum': forum, 'post_form': post_form
    })


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ForumCreate(CreateView):
    model = Forum
    fields = ['title', 'author', 'comment', 'spookyLevel']


class ForumUpdate(LoginRequiredMixin, UpdateView):
    model = Forum
    fields = ['author', 'comment', 'spookyLevel']


class ForumDelete(LoginRequiredMixin, DeleteView):
    model = Forum
    success_url = '/forums/'


@login_required
def add_posts(request, forum_id, user_id):
    form = PostsForm(request.POST)
    if form.is_valid():
        new_posts = form.save(commit=False)
        new_posts.forum_id = forum_id
        new_posts.user_id = user_id
        new_posts.save()
    return redirect("forums_index")


class PostCreate(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['date', 'title', 'author', 'date',
              'comment', 'topic', 'spookyLevel', 'description']
    

class PostList(LoginRequiredMixin, ListView):
    model = Posts


class PostDetail(LoginRequiredMixin, DetailView):
    model = Posts


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Posts
    fields = ['date', 'title', 'author', 'date','comment', 'topic', 'spookyLevel', 'description']
   

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Posts
    success_url = '/posts/'


def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('forums_index')
    else:
      error_message = 'Invalid sign up! Try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
