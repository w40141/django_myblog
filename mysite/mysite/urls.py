"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from blog.views import post_list, post_detail
# from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/<int:post_id>", include("blog.urls"),),
    path("", include("blog.urls")),
    # path(
    #     "posts/<int:post_id>/",
    #     PostDetailView.as_view(),
    #     name="post_detail",
    # ),
    # path("", PostListView.as_view(), name="post_list"),
    # path("posts/<int:post_id>/", post_detail, name="post_detail"),
    # path("", post_list, name="post_list"),
]
