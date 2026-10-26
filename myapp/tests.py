from django.test import TestCase
from django.urls import reverse, resolve

from myapp import views

#add tests for your views and models here.

class HomeViewTests(TestCase):
    def test_home_url_resolves_to_home_view(self):
        self.assertEqual(resolve('/').func, views.home)

    def test_home_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Hello, World!')


class AboutViewTests(TestCase):
    def test_about_url_resolves_to_about_view(self):
        self.assertEqual(resolve('/about/').func, views.about)

    def test_about_returns_200(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About Page')


class MissingPageTests(TestCase):
    def test_unknown_url_returns_404(self):
        response = self.client.get('/does-not-exist/')
        self.assertEqual(response.status_code, 404)
