from django.urls import reverse_lazy
from django.views import generic

from .forms import PostCreateForm
from .models import Post


class PostListView(generic.ListView):
    """post list view"""

    model = Post
    ordering = "-created_at"
    # template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    """description"""

    model = Post
    pk_url_kwarg = "post_id"
    # template_name = "post_detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):

    model = Post
    form_class = PostCreateForm
    # template_name = "post_create.html"
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(generic.UpdateView):
    """description"""

    model = Post
    pk_url_kwarg = "post_id"
    form_class = PostCreateForm
    # template_name = "post_create.html"
    success_url = reverse_lazy('blog:post_detail')


class PostDeleteView(generic.DeleteView):
    """description"""

    model = Post
    pk_url_kwarg = "post_id"
    # template_name = "post_create.html"
    success_url = reverse_lazy('blog:post_list')
