from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse
from .models import Post
# Create your tests here.
User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(username="TestUser")
        return test_user

    def test_post_item(self):
        post = Post.objects.create(
            user=User.objects.first(),
            content='Some test content'
        )
        self.assertTrue(post.user.username == 'TestUser')
        self.assertTrue(post.content == 'Some test content')

    def test_post_url(self):
        post = Post.objects.create(
            user=User.objects.first(),
            content="Some test content"
        )
        absolute_url = reverse("posts:post_detail", kwargs={"pk": post.pk})
        self.assertEqual(post.get_absolute_url(), absolute_url)
