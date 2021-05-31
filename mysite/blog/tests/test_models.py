from django.test import TestCase
from ..models import Post


class PostModelTests(TestCase):

    # def test_is_empty(self):
    #     saved_posts = Post.objects.all()
    #     self.assertEqual(saved_posts.count, 0)

    def test_saving_and_retrieving_post(self):
        post = Post()
        title = "test_title_to_retrieve"
        body = "test_body_to_retrieve"
        post.title = title
        post.body = body
        post.save()

        saved_posts = Post.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.title, title)
        self.assertEqual(actual_post.body, body)
