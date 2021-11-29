from django.forms import ModelForm
from .models import Posts


class PostsForm(ModelForm):
  class Meta:
    model = Posts
    fields = ["date", "topic", "title", "author", "comment", "spookyLevel"]
