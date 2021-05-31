from django.test import TestCase
from django.urls import resolve
from ..views import PostListView, PostDetailView


class TestUrls(TestCase):

    def test_post_list_url(self):
        view = resolve("/blog/")
        self.assertEqual(view.func.view_class, PostListView)

    def test_post_detail_url(self):
        view = resolve("/blog/detail/<int:post_id>/")
        self.assertEqual(view.func.view_class, PostDetailView)
