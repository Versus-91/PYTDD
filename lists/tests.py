from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_bad_maths(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")
