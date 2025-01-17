from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_template_name_correct(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, 'home.html')

    def test_heading_content(self):
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, '<h1>Message board homepage</h1>')
    
    def test_model_dynamic_content(self):
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, '<li>This is a test!</li>')

