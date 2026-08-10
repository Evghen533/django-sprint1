# blog/test/test_views.py
from django.test import TestCase
from blog.models import Post, Category
from django.utils import timezone
from datetime import datetime
from django.urls import reverse


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat_travel = Category.objects.create(title="Travel", slug="travel")
        cls.cat_adventure = Category.objects.create(
            title="Adventure", slug="adventure"
        )
        cls.cat_city = Category.objects.create(title="City", slug="city")
        cls.cat_not_my_day = Category.objects.create(
            title="Not My Day", slug="not-my-day"
        )

        posts = [
            Post(
                title="Шторм и крушение",
                content="Текст первого поста",
                created_at=timezone.make_aware(datetime(2025, 1, 1, 10, 0, 0)),
                is_published=True,
                category=cls.cat_travel,
            ),
            Post(
                title="Корабль сняло с мели",
                content="Текст второго поста",
                created_at=timezone.make_aware(datetime(2025, 1, 2, 11, 0, 0)),
                is_published=True,
                category=cls.cat_adventure,
            ),
            Post(
                title="Третий пост",
                content="Текст третьего поста",
                created_at=timezone.make_aware(datetime(2025, 1, 3, 12, 0, 0)),
                is_published=True,
                category=cls.cat_city,
            ),
            Post(
                title="Дождь и ветер",
                content="Плохой день на море",
                created_at=timezone.make_aware(datetime(2025, 1, 4, 9, 0, 0)),
                is_published=True,
                category=cls.cat_not_my_day,
            ),
        ]
        Post.objects.bulk_create(posts)

    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Шторм и крушение")

    def test_post_detail_valid(self):
        for post in Post.objects.all():
            url = reverse('blog:post_detail', args=[post.pk])
            response = self.client.get(url)
            self.assertEqual(
                response.status_code,
                200,
                f"Post {post.pk} status (url={url})",
            )

    def test_post_detail_invalid(self):
        url = reverse('blog:post_detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_category_travel(self):
        response = self.client.get("/category/travel/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Шторм и крушение")
        self.assertNotContains(response, "Корабль сняло с мели")

    def test_category_not_my_day(self):
        response = self.client.get("/category/not-my-day/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Дождь и ветер")
        self.assertNotContains(response, "Шторм и крушение")
