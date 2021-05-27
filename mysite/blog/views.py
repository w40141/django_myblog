# from django.shortcuts import get_object_or_404
# # from django.template.loader import render_to_string
# # from django.http import Http404
# from blog.models import Post
# from django.template.response import TemplateResponse
#
#
# def post_list(request):
#     # body = "<br>".join([p.title for p in Post.objects.all()])
#     # body = render_to_string(
#     #     "post_list.html",
#     #     {"posts": Post.objects.all()},
#     # )
#     # return HttpResponse(body)
#     return TemplateResponse(request, "post_list.html", {"posts": Post.objects.all()})
#
#
# def post_detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(id=post_id)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, id=post_id)
#     return TemplateResponse(request, "post_detail.html", {"post": post})

from django.views.generic import DetailView, ListView
from blog.models import Post


class PostListView(ListView):
    """post list view"""

    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """description"""

    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"
