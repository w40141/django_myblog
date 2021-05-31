from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("detail/<int:post_id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("update/<int:post_id>/", views.PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:post_id>/", views.PostDeleteView.as_view(), name="post_delete"),
]
