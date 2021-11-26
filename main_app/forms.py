from django.forms import ModelForm, fields
from .models import Posts


class PostsForm(ModelForm):
  class Meta:
    model = Posts
    fields = ["date", "topic"]
