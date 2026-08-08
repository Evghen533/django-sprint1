from django.test import TestCase
from django.urls import reverse


class PagesViewsTest(TestCase):
    def test_about_page_status_and_template(self):
        url = reverse('pages:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
        self.assertContains(response, 'О нас')

    def test_rules_page_status_and_template(self):
        url = reverse('pages:rules')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/rules.html')
        self.assertContains(response, 'Правила сайта')
