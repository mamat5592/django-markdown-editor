# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="my title", description="blurb", wiki="post body")
        self.assertEqual(post.title, "my title")
        self.assertEqual(post.description, "blurb")
        self.assertEqual(post.wiki, "post body")
