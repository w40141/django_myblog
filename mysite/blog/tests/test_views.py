from django.test import TestCase
from django.urls import reverse
from ..models import Post


class IndexTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)


class PostListTests(TestCase):
    """"""

    def setUp(self):
        post1 = Post.objects.create(title="title1", body="body1")
        post2 = Post.objects.create(title="title2", body="body2")

    def test_get(self):
        response = self.client.get(reverse("blog:detail"))
        self.assertEqual(response.status_code, 200)

    def test_get_2posts_by_list(self):
        response = self.client.get(reverse("blog:detail"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["detail"],
            ["<Post: title1>", "<Post: title2>"],
            orderd=False,
        )
        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')

    def tearDown(self):
        post1 = Post.objects.create(title='title1', body='body1')
        post2 = Post.objects.create(title='title2', body='body2')
