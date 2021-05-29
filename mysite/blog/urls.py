from django.urls import path
from . import views

urlpatterns = [
    path(
        "posts/<int:post_id>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path("", views.PostListView.as_view(), name="post_list"),
]
