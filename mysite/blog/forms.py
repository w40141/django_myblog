from .models import Post
from django.forms import ModelForm


class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        fields = ("title", "body")
